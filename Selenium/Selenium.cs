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

        //[SetUp]
        //public void SetupTest()
        //{
        //    driver = new FirefoxDriver();
        //}

        //[TearDown]
        //public void TearDownTest()
        //{
        //    driver.Close();
        //}

        private void AssertPoints(int points)
        {
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(15));
            wait.Until(x => driver.FindElement(By.Id("points")).Text != "");
            Thread.Sleep(500);
            var pointsValue = driver.FindElement(By.Id("points")).Text;
            Assert.AreEqual(pointsValue, points.ToString(), "Points error");
        }

        //[Test(Description = "Start browsing")]
        //public void TestExercises()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000");
        //    var startButton = driver.FindElement(By.LinkText("Rozpocznij"));
        //    startButton.Click();
        //    var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(15));
        //    wait.Until(x => x.FindElement(By.Id("exercise")));
        //    Assert.IsTrue(driver.FindElements(By.Id("exercise")).Count > 0);
        //    driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
        //    var answers = "ABBDBCCCDDAADACADBCABDBCA";
        //    foreach(var answerChar in answers)
        //    {
        //        var answer = answerChar.ToString();
        //        wait.Until(x => driver.FindElement(By.Id(answer)).Displayed);
        //        driver.FindElement(By.Id(answer)).Click();
        //        Next();
        //    }

        //    var points = 25;
        //    AssertPoints(points);
        //    ManyValues(new[] {"5", "3", "-3"});
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    Intervals();
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    Proof(new[] {"0", "1", "2", "3"});
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    Proof(new[] {"0", "1", "2", "3", "4", "5", "6"});
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    SingleValue("36%");
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    SingleValue("2sqrt(17)");
        //    Next();
        //    points += 2;
        //    AssertPoints(points);
        //    ListOfValues(new []{"26","27"});
        //    Next();
        //    points += 4;
        //    AssertPoints(points);
        //    ListOfValues(new []{"20.4","-2.8"});
        //    Next();
        //    points += 4;
        //    AssertPoints(points);
        //    SingleValue("sqrt(5)/5");
        //    points += 5;
        //    AssertPoints(points);
        //}

        //void ListOfValues(string[] answers)
        //{
        //    var inputs = driver.FindElements(By.TagName("input"));
        //    for (var i = 0; i < answers.Length; i++)
        //    {
        //        Thread.Sleep(50);
        //        inputs[i].SendKeys(answers[i]);
        //    }
        //    driver.FindElement(By.Id("submit-answer")).Click();
        //    Thread.Sleep(500);
        //    var success = driver.FindElements(By.ClassName("bg-success")).Count;
        //    Assert.AreEqual(success, answers.Length+1);
        //}

        //private void Next()
        //{
        //    driver.FindElement(By.LinkText("Następny")).Click();
        //    Thread.Sleep(100);
        //}

        //[Test(Description = "Get Exercise 26")]
        //public void TestExercise26()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000/1/26");
        //    AssertPoints(0);
        //    ManyValues(new[] {"5", "3", "-3"});
        //    Thread.Sleep(500);
        //    AssertPoints(2);
        //}

        //[Test(Description = "Get Exercise 26")]
        //public void TestExercise27()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000/1/27");
        //    AssertPoints(0);
        //    Intervals();
        //    Thread.Sleep(500);
        //    AssertPoints(2);
        //}

        //private static SelectElement Select(IWebElement element)
        //{
        //    var select = new SelectElement(element);
        //    return select;
        //}

        //private void Intervals()
        //{
        //    var select = driver.FindElement(By.Id("interval-number-select"));
        //    var y = new SelectElement(select);
        //    y.SelectByText("2");
        //    driver.FindElements(By.TagName("input"))[0].SendKeys("4/3");
        //    driver.FindElements(By.TagName("input"))[1].SendKeys("4/3");
        //    driver.FindElements(By.TagName("input"))[2].SendKeys("4");
        //    driver.FindElements(By.TagName("input"))[3].SendKeys("4");

        //    Select(driver.FindElements(By.TagName("select"))[1]).SelectByValue("left-inf");
        //    Select(driver.FindElements(By.TagName("select"))[2]).SelectByValue("right-open");

        //    Select(driver.FindElements(By.TagName("select"))[3]).SelectByValue("left-open");
        //    Select(driver.FindElements(By.TagName("select"))[4]).SelectByValue("right-inf");

        //    driver.FindElement(By.Id("submit-answer")).Click();

        //    var success = driver.FindElements(By.ClassName("bg-success")).Count;
        //    Assert.AreEqual(success, 10);
        //}

        //private void ManyValues(string[] answers)
        //{
        //    var select = driver.FindElement(By.Id("number-answers"));
        //    var y = new SelectElement(select);
        //    y.SelectByText(answers.Length.ToString());
        //    var inputs = driver.FindElements(By.TagName("input"));
        //    for (var i = 0; i < answers.Length; i++) inputs[i].SendKeys(answers[i]);
        //    driver.FindElement(By.Id("submit-answer")).Click();
        //    Thread.Sleep(100);

        //    var exercise = driver.FindElement(By.Id("exercise"));
        //    var successNum = exercise.FindElements(By.ClassName("bg-success")).Count;
        //    Assert.IsTrue(successNum == answers.Length + 2, "Wrong number of success class");
        //}

        //private void Proof(string[] answers)
        //{
        //    foreach (var answer in answers)
        //    {
        //        driver.FindElement(By.Id(answer)).Click();
        //        Thread.Sleep(500);
        //    }

        //    driver.FindElement(By.Id("submit-answer")).Click();
        //    var correct = driver.FindElements(By.ClassName("bg-success")).Count;
        //    Assert.AreEqual(correct, answers.Length + 1);
        //}

        //[Test]
        //public void TestExercise28()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000/1/28");
        //    AssertPoints(0);
        //    Proof(new[] {"0", "1", "2", "3"});
        //    AssertPoints(2);
        //}

        //[Test]
        //public void TestExercise29()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000/1/29");
        //    AssertPoints(0);
        //    Proof(new[] {"0", "1", "2", "3", "4", "5", "6"});
        //    AssertPoints(2);
        //}

        //[Test]
        //public void TestExercise30()
        //{
        //    driver.Navigate().GoToUrl("http://localhost:8000/1/30");
        //    AssertPoints(0);
        //    SingleValue("36%");
        //    AssertPoints(2);
        //}


        //public void SingleValue(string value)
        //{
        //    driver.FindElement(By.TagName("input")).SendKeys(value);
        //    driver.FindElement(By.Id("submit-answer")).Click();
        //    Thread.Sleep(500);
        //    var success = driver.FindElements(By.ClassName("bg-success")).Count;
        //    Assert.AreEqual(success, 2);
        //}
    }
}