using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

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
            //driver.Close();
        }

        [Test(Description = "Start browsing")]
        public void TestExercises()
        {

            driver.Navigate().GoToUrl("http://localhost:8000");
            var startButton = driver.FindElement(By.LinkText("Rozpocznij"));
            startButton.Click();
            var wait = new WebDriverWait(driver, System.TimeSpan.FromSeconds(1));
            wait.Until(x => x.FindElement(By.Id("exercise")));
            Assert.IsTrue(driver.FindElements(By.Id("exercise")).Count>0);
            driver.FindElement(By.Id("A")).Click();
            driver.FindElement(By.Id("submit-answer")).Click();;
        }



    }

}

