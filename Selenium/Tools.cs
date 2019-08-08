using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

namespace Selenium
{
    public static class Tools
    {
        public static Process RunServer(string port, string admin_login, string admin_pass)
        {
            var startupPath = Environment.CurrentDirectory;
            var array = startupPath.Split('\\').ToArray();
            array = array.Reverse().Skip(3).Reverse().ToArray();
            startupPath = @"C:\Users\cheshire\OneDrive\Documents\GitHub\Cerebri.pl\Cerebri";
            Directory.SetCurrentDirectory(startupPath);
            Process.Start("python", "manage.py flush --settings=system.test_settings --no-input");
            Process.Start("python", "manage.py migrate --settings=system.test_settings");
            var script = "from django.contrib.auth.models import User;";
            script += $"User.objects.create_superuser('{admin_login}', 'admin@example.com', '{admin_pass}')";
            Process.Start("python", $"manage.py shell --settings=system.test_settings -c \"{script}\"");
            var resultProcess = Task.Run(() =>
                Process.Start("python", $"manage.py runserver {port} --settings=system.test_settings")).Result;
            return resultProcess;
        }

        public static void OpenExercise(FirefoxDriver driver)
        {
            driver.FindElementsByClassName("start-course").Last().Click();
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("exercise-title").Displayed);
            Assert.IsTrue(driver.FindElementById("exercise-title").Displayed);
            Assert.IsTrue(driver.FindElementById("exercise-description").Displayed);
        }

        public static void EditExercise(FirefoxDriver driver, string answerType)
        {
            driver.FindElementById("exercise-edit").Click();

            var points = "5";
            var titleText = "xyz";
            var descriptionText = "abc";

            driver.FindElementById("title-input").Clear();
            driver.FindElementById("title-input").SendKeys(titleText);

            driver.FindElementById("points-input").Clear();
            driver.FindElementById("points-input").SendKeys(points);

            driver.ExecuteScript($"editor.setValue(`{descriptionText}`);");

            switch (answerType)
            {
                case "AnswersType.Closed":
                    TestClosed(driver);
                    break;
                case "AnswersType.ManyValues":
                    TestManyValues(driver);
                    break;
                case "AnswersType.Proof":
                    TestProof(driver);
                    break;
                case "AnswersType.ListOfValues":
                    TestListOfValues(driver);
                    break;
                case "AnswersType.Intervals":
                    TestIntervals(driver);
                    break;
                default:
                    driver.FindElementById("show-button").Click();
                    break;
            }

            var text = driver.FindElementById("exercise-title").Text;
            Assert.IsTrue(text.Contains(titleText));
            Assert.AreEqual(driver.FindElementById("exercise-description").Text, descriptionText);
            var pointsValue = driver.FindElementById("points").Text;
            Assert.AreEqual(pointsValue, points);
        }

        public static void TestClosed(FirefoxDriver driver)
        {
            driver.FindElementById("answer-A").Clear();
            driver.FindElementById("answer-A").SendKeys("answer A");
            driver.FindElementById("answer-B").Clear();
            driver.FindElementById("answer-B").SendKeys("answer B");
            driver.FindElementById("answer-C").Clear();
            driver.FindElementById("answer-C").SendKeys("answer C");
            driver.FindElementById("answer-D").Clear();
            driver.FindElementById("answer-D").SendKeys("answer D");
            driver.FindElementById("radio-answer-C").Click();


            driver.FindElementById("show-button").Click();
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("C").Displayed);

            Assert.AreEqual(driver.FindElementById("A").Text, "answer A");
            Assert.AreEqual(driver.FindElementById("B").Text, "answer B");
            Assert.AreEqual(driver.FindElementById("C").Text, "answer C");
            Assert.AreEqual(driver.FindElementById("D").Text, "answer D");

            driver.FindElementById("C").Click();
            Assert.IsTrue(driver.FindElementById("C").GetAttribute("class").Contains("btn-success"));
        }


        class AnswerInterval
        {
            public string leftType;
            public string leftValue;
            public string rightType;
            public string rightValue;

            public string GetTab()
            {
                return $"['{leftValue}', '{leftType}', '{rightValue}', '{rightType}']";
            }
        }

        private static void TestIntervals(FirefoxDriver driver)
        {
            var answerSelect = driver.FindElementById("answer-type");
            var selectElement = new SelectElement(answerSelect);
            selectElement.SelectByValue("4");

            var answerList = new List<AnswerInterval>
            {
                new AnswerInterval {leftType = "left-inf", leftValue = "-inf", rightType="right-open", rightValue = "4/3"},
                new AnswerInterval {leftType = "left-open", leftValue = "4", rightType="right-inf", rightValue = "inf"},
            };

            var answersText = $"{{'num_answers': [0, 1, 2], 'answers': [{answerList[0].GetTab()}, {answerList[1].GetTab()}]}}";


            var text = $"answersEditor.setValue(`{answersText}`);";

            driver.ExecuteScript(text);
            driver.FindElementById("show-button").Click();

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("interval-number-select").Displayed);

            var numberSelect = driver.FindElementById("interval-number-select");
            var select = new SelectElement(numberSelect);
            select.SelectByText("2");

            var Intervals = driver.FindElementsByClassName("interval-div");

            Assert.AreEqual(Intervals.Count, answerList.Count);

            for(var i=0;i<Intervals.Count;i++)
            {
                var interval = Intervals[i];
                var answer = answerList[i];

                var fromDiv = interval.FindElement(By.ClassName("interval-from")).FindElement(By.TagName("input"));
                var toDiv = interval.FindElement(By.ClassName("interval-to")).FindElement(By.TagName("input"));

                var leftInterval = interval.FindElement(By.ClassName("interval-type-left"));
                var rightInterval = interval.FindElement(By.ClassName("interval-type-right"));

                var leftSelect = new SelectElement(leftInterval);
                var rightSelect = new SelectElement(rightInterval);

                leftSelect.SelectByValue(answer.leftType);
                rightSelect.SelectByValue(answer.rightType);

                if (answer.leftType != "left-inf")
                {
                    fromDiv.SendKeys(answerList[i].leftValue);
                }

                if (answer.rightType != "right-inf")
                {
                    toDiv.SendKeys(answerList[i].rightValue);
                }
            }

            driver.FindElementById("submit-answer").Click();

            var numSuccess = driver.FindElementsByClassName("bg-success").Count;
            Assert.AreEqual(numSuccess, answerList.Count*4+2);
        }

        public static void TestManyValues(FirefoxDriver driver)
        {
            var answerSelect = driver.FindElementById("answer-type");
            var selectElement = new SelectElement(answerSelect);
            selectElement.SelectByValue("1");
            var answersText = "{ 'num_answers': [0, 1, 2, 3],'answers': [10, 20, 30] }";
            driver.ExecuteScript($"answersEditor.setValue(`{answersText}`);");

            driver.FindElementById("show-button").Click();

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("number-answers").Displayed);

            var numAnswers = driver.FindElementById("number-answers");
            var numSelect = new SelectElement(numAnswers);
            numSelect.SelectByValue("3");

            var inputs = driver.FindElementsByTagName("input");
            var answers = new[]{10,20,30};

            for (var i = 0; i < inputs.Count; i++)
            {
                inputs[i].SendKeys(answers[i].ToString());
            }

            driver.FindElementById("submit-answer").Submit();

            var numSuccess = driver.FindElementsByClassName("bg-success").Count;
            Assert.AreEqual(2+answers.Length, numSuccess);

        }

        private static void TestListOfValues(FirefoxDriver driver)
        {
            var answerSelect = driver.FindElementById("answer-type");
            var selectElement = new SelectElement(answerSelect);
            selectElement.SelectByValue("3");

            var answersText = @"[{'description': 'Wartość', 'id': 'x-value', 'value': 'sqrt(5) / 5'}]";
            driver.ExecuteScript($"answersEditor.setValue(`{answersText}`);");

            driver.FindElementById("show-button").Click();

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("x-value").Displayed);

            driver.FindElementById("x-value").SendKeys("1/sqrt(5)");
            driver.FindElementById("submit-answer").Click();

            var numSuccess = driver.FindElementsByClassName("bg-success").Count;

            Assert.AreEqual(2, numSuccess);
        }

        private static void TestProof(FirefoxDriver driver)
        {

            var answerSelect = driver.FindElementById("answer-type");
            var selectElement = new SelectElement(answerSelect);
            selectElement.SelectByValue("2");

            var answersText =
                "{'steps': [{'id': '0', 'value': 'A'},{'id': '1', 'value': 'B'},{'id': '2', 'value': 'C'},], 'correct_sequences': [['0','1','2']] }";

            driver.ExecuteScript($"answersEditor.setValue(`{answersText}`);");

            driver.FindElementById("show-button").Click();

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementById("0").Displayed);

            driver.FindElementById("0").Click();
            driver.FindElementById("1").Click();
            driver.FindElementById("2").Click();


            driver.FindElementById("submit-answer").Click();
            var numSuccess = driver.FindElementsByClassName("bg-success").Count;
            Assert.AreEqual(4, numSuccess);

        }


        public static void AdminLogin(FirefoxDriver driver, string port = "8888", string admin_login = "admin",
            string admin_pass = "pass1234")
        {
            var url = $"http://localhost:{port}/admin";
            driver.Navigate().GoToUrl(url);
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            driver.FindElementById("id_username").SendKeys(admin_login);
            driver.FindElementById("id_password").SendKeys(admin_pass);
            driver.FindElementByXPath("//input[@type='submit']").Click();
        }

        public static void GoHome(FirefoxDriver driver, string port = "8888")
        {
            var url = $"http://localhost:{port}/";
            driver.Navigate().GoToUrl(url);
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => c.FindElement(By.TagName("body")));
        }

        public static void CreateCourse(FirefoxDriver driver, string courseTitle = "Test title",
            string courseDescription = "Test description")
        {
            AdminLogin(driver);
            GoHome(driver);

            driver.FindElement(By.Id("add-course")).Click();
            driver.FindElement(By.Id("title-input")).SendKeys(courseTitle);
            driver.FindElement(By.Id("description-input")).SendKeys(courseDescription);
            driver.FindElement(By.Id("add-course")).Click();
            GoHome(driver);

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementByClassName("course-title") != null);
            Assert.IsTrue(driver.FindElementByClassName("course-title").Displayed);
            Assert.IsTrue(driver.FindElementByClassName("course-description").Displayed);

            Assert.AreEqual(driver.FindElementByClassName("course-title").Text, courseTitle);
            Assert.AreEqual(driver.FindElementByClassName("course-description").Text, courseDescription);
        }
    }
}