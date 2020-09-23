const { Builder, By, Key, Until } = require('selenium-webdriver');

async function example(){
   let driver = new Builder().forBrowser('firefox').build();
   try {
      await driver.manage().window().maximize();
      await driver.get('https://www.google.com');
      await driver.findElement(By.name('q')).sendKeys('Selenium Tutorial');
   } finally {
      await driver.quit()
   }
}

example()
