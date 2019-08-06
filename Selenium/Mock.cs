using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

namespace Selenium
{
    [TestFixture]
    public class Mock
    {
        private FirefoxDriver driver;

        [SetUp]
        public void SetupTest()
        {
            RunServer();
            driver = new FirefoxDriver();
        }

        [TearDown]
        public void TearDownTest()
        {
            driver.Close();
            resultProcess.CloseMainWindow();
        }

        private Process resultProcess;

        [Test]
        public void ConnectionTest()
        {
            var url = "http://localhost:8000/";
            driver.Navigate().GoToUrl(url);
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            wait.Until(c => c.FindElement(By.TagName("body")));
            Assert.IsTrue(driver.FindElement(By.TagName("body")).Displayed);
        }

        [Test]
        public void AdminTest()
        {
            var url = "http://localhost:8000/admin";
            driver.Navigate().GoToUrl(url);
            var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
            driver.FindElementById("id_username").SendKeys("admin");
            driver.FindElementById("id_password").SendKeys("adminpass");
            driver.FindElementByXPath("//input[@type='submit']").Click();
            Assert.IsTrue(driver.FindElementByXPath("//*[text()='Administracja stroną']").Displayed);
        }

        private void RunServer()
        {
            var startupPath = Environment.CurrentDirectory;
            var array = startupPath.Split('\\').ToArray();
            array = array.Reverse().Skip(3).Reverse().ToArray();
            startupPath = @"C:\Users\cheshire\OneDrive\Documents\GitHub\Cerebri.pl\Cerebri";
            Directory.SetCurrentDirectory(startupPath);
            Process.Start("python", "manage.py flush --settings=system.test_settings --no-input");
            Process.Start("python", "manage.py migrate --settings=system.test_settings");
            var script = "from django.contrib.auth.models import User;";
            script += "User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')";
            Process.Start("python", $"manage.py shell --settings=system.test_settings -c \"{script}\"");
            resultProcess =
                Task.Run(() => Process.Start("python", "manage.py runserver --settings=system.test_settings")).Result;
        }
    }
}