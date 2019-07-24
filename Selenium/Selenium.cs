using System;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;
using System.Threading;

namespace Selenium
{

    [TestFixture]
    public class FirefoxSampleTest
    {
        private IWebDriver driver;
        
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

        void AssertPoints(int points)
        {
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(15));
            wait.Until(x => driver.FindElement(By.Id("points")).Text != "");
            Thread.Sleep(500);
            var pointsValue = driver.FindElement(By.Id("points")).Text;
            Assert.AreEqual(pointsValue, points.ToString(), "Points error");
        }

        [Test(Description = "Start browsing")]
        public void TestExercises()
        {

            driver.Navigate().GoToUrl("http://localhost:8000");
            var startButton = driver.FindElement(By.LinkText("Rozpocznij"));
            startButton.Click();
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(15));
            wait.Until(x => x.FindElement(By.Id("exercise")));
            Assert.IsTrue(driver.FindElements(By.Id("exercise")).Count>0); driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);

            for (var i = 0; i < 25; i++)
            {
                wait.Until(x => driver.FindElement(By.Id("A")).Displayed);
                driver.FindElement(By.Id("A")).Click();
                driver.FindElement(By.LinkText("Następny")).Click();
            }
            AssertPoints(7);
            ManyValues(new[] { "5", "3", "-3" }); 
            driver.FindElement(By.LinkText("Następny")).Click();
            AssertPoints(9);
            Intervals();
            driver.FindElement(By.LinkText("Następny")).Click();
            AssertPoints(11);
            Proof(new[] {"0", "1", "2", "3"});
            driver.FindElement(By.LinkText("Następny")).Click();
            AssertPoints(13);
            Proof(new[] {"0", "1", "2", "3","4","5","6"});
            driver.FindElement(By.LinkText("Następny")).Click();
            AssertPoints(15);

        }

        [Test(Description = "Get Exercise 26")]
        public void TestExercise26()
        {

            driver.Navigate().GoToUrl("http://localhost:8000/test/26");
            AssertPoints(0);
            ManyValues(new[] { "5", "3", "-3" }); 
            Thread.Sleep(500);
            AssertPoints(2);
        }

        [Test(Description = "Get Exercise 26")]
        public void TestExercise27()
        {

            driver.Navigate().GoToUrl("http://localhost:8000/test/27");
            AssertPoints(0);
            Intervals();
            Thread.Sleep(500);
            AssertPoints(2);
        }

        static SelectElement Select(IWebElement element)
        {
            var select = new SelectElement(element);
            return select;
        }

        void Intervals()
        {
            var select = driver.FindElement(By.Id("interval-number-select"));
            var y = new SelectElement(select);
            y.SelectByText("2");
            driver.FindElements(By.TagName("input"))[0].SendKeys("4/3");
            driver.FindElements(By.TagName("input"))[1].SendKeys("4/3");
            driver.FindElements(By.TagName("input"))[2].SendKeys("4");
            driver.FindElements(By.TagName("input"))[3].SendKeys("4");

            Select(driver.FindElements(By.TagName("select"))[1]).SelectByValue("left-inf");
            Select(driver.FindElements(By.TagName("select"))[2]).SelectByValue("right-open");   
            
            Select(driver.FindElements(By.TagName("select"))[3]).SelectByValue("left-open");
            Select(driver.FindElements(By.TagName("select"))[4]).SelectByValue("right-inf");

            driver.FindElement(By.Id("submit-answer")).Click();

            var success = driver.FindElements(By.ClassName("bg-success")).Count;
            Assert.AreEqual(success, 10);
        }

        void ManyValues(string[] answers)
        {
            var select = driver.FindElement(By.Id("number-answers"));
            var y = new SelectElement(select);
            y.SelectByText("3");
            var inputs = driver.FindElements(By.TagName("input"));
            for (var i = 0; i < answers.Length; i++)
            {
                inputs[i].SendKeys(answers[i]);
            }
            driver.FindElement(By.Id("submit-answer")).Click();
            Thread.Sleep(100);

            var exercise = driver.FindElement(By.Id("exercise"));
            var successNum = exercise.FindElements(By.ClassName("bg-success")).Count;
            Assert.IsTrue(successNum == answers.Length+2, "Wrong number of success class");

        }

        void Proof(string[] answers)
        {
            foreach (var answer in answers)
            {
                driver.FindElement(By.Id(answer)).Click();
                Thread.Sleep(500);
            }
            driver.FindElement(By.Id("submit-answer")).Click();
            var correct = driver.FindElements(By.ClassName("bg-success")).Count;
            Assert.AreEqual(correct, answers.Length+1);
        }

        [Test]
        public void TestExercise28()
        {
            driver.Navigate().GoToUrl("http://localhost:8000/test/28");
            AssertPoints(0);
            Proof(new []{"0","1","2","3"});
            AssertPoints(2);
        }

        [Test]
        public void TestExercise29()
        {
            driver.Navigate().GoToUrl("http://localhost:8000/test/29");
            AssertPoints(0);
            Proof(new []{"0","1","2","3","4","5","6"});
            AssertPoints(2);
        }
    }

}

