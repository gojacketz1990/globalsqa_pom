# Header Setup and Information

## Page Object Locators
All links that are housed in the header are shared by each page.  To call the header links through the instantiated page each page object class will need to import the header component:

from pages.HeaderComponents import HeaderComponent

    from pages.HeaderComponents import HeaderComponent

Now the actual test file can call the links through the current page and return the new page:

    authenticationPage = cardCatalogHome.header.navigate_authenticate()

So from the catalog home page you click on navigation which returns the authenticationPage


