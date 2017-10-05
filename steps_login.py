def iniciar_driver():
    if not hasattr(world, 'driver'):
        #world.driver = webdriver.Chrome("chromedriver")
        world.driver = webdriver.Firefox()
    else:
        world.driver.get("http://148.217.200.108/application/index.php?mod=usuarios&controlador=login&accion=logout")
    world.driver.implicitly_wait(1)