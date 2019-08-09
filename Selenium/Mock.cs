using System;
using System.Diagnostics;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

namespace Selenium
{

    [TestFixture]
    public class Mock
    {
        private string port = "8888";
        private FirefoxDriver driver;
        private string admin_login = "admin";
        private string admin_pass = "pass1234";
        private Process resultProcess;


        [OneTimeSetUp]
        public void GlobalSetup()
        {
            resultProcess = Tools.RunServer(port, admin_login, admin_pass);
        }

        [OneTimeTearDown]
        public void GlobalTeardown()
        {
            resultProcess.CloseMainWindow();
        }

        [SetUp]
        public void SetupTest()
        {
            driver = new FirefoxDriver();
        }

        [TearDown]
        public void TearDownTest()
        {
            driver.Close();
        }

        [Test]
        public void AddCourseTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
        }

        [Test]
        public void EditExerciseClosedTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
            Tools.EditExercise(driver, "AnswersType.Closed");
        }

        [Test]
        public void EditExerciseManyValuesTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
            Tools.EditExercise(driver, "AnswersType.ManyValues");
        }

        [Test]
        public void EditExerciseProofTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
            Tools.EditExercise(driver, "AnswersType.Proof");
        }

        [Test]
        public void EditExerciseListOfValuesTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
            Tools.EditExercise(driver, "AnswersType.ListOfValues");
        }

        [Test]
        public void EditExerciseIntervalsTest()
        {
            Tools.CreateCourse(driver);
            Tools.OpenExercise(driver);
            Tools.EditExercise(driver, "AnswersType.Intervals");
        }

        //[Test]
        //public void ConnectionTest()
        //{
        //    Tools.GoHome(driver);
        //    Assert.IsTrue(driver.FindElement(By.TagName("body")).Displayed);
        //}

        //[Test]
        //public void AdminTest()
        //{
        //    Tools.AdminLogin(driver, port, admin_login, admin_pass);
        //    Assert.IsTrue(driver.FindElementByXPath("//*[text()='Administracja stroną']").Displayed);
        //}

        [Test]
        public void AddManyExercisesOCR()
        {
            var courseTitle = "xyz";
            var courseDescription = "abc";

            Tools.AdminLogin(driver);
            Tools.GoHome(driver);
            driver.FindElement(By.Id("add-course")).Click();
            driver.FindElement(By.Id("title-input")).SendKeys(courseTitle);
            driver.FindElement(By.Id("description-input")).SendKeys(courseDescription);

            //driver.FindElementById("clickHere").Click();

            var dir = @"C:\Users\cheshire\OneDrive\Documents\GitHub\Cerebri.pl\Selenium\test-exercises";

            var fileDir1 = $@"{dir}\zadanie-001.png";
            var fileDir2 = $@"{dir}\zadanie-002.png";
            var fileDir3 = $@"{dir}\zadanie-003.png";
            
            driver.FindElementById("file").SendKeys(fileDir1);
            driver.FindElementById("file").SendKeys(fileDir2);
            driver.FindElementById("file").SendKeys(fileDir3);


            driver.FindElementById("send-exercises").Click();

            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => driver.FindElementsByClassName("exercise-content").Count != 0);

            var i = 1;
            foreach (var textArea in driver.FindElementsByClassName("exercise-content"))
            {
                textArea.Clear();
                textArea.SendKeys($"Exercise {i++}");
            }

            driver.FindElementById("send-exercises").Click();

            for (i = 1; i < 4; i++)
            {
                wait.Until(c => driver.FindElementsById("exercise-description").Count != 0);
                wait.Until(c => driver.FindElementById("exercise-description").Displayed);

                var descriptionText = driver.FindElementById("exercise-description").Text;
                Assert.AreEqual($"Exercise {i}", descriptionText);

                if (i < 3) driver.FindElementById("next-exercise").Click();
            }

            Assert.AreEqual(0, driver.FindElementsById("next-exercise").Count);
            Assert.AreEqual(1, driver.FindElementsById("end-course").Count);
        }
    }
}