# -*- coding: utf-8 -*-

from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

'''
--------------------------------------------------------------------------------
Inicia pruebas login
--------------------------------------------------------------------------------
'''


@step(u'Dado que yo tecleo en el campo usuario "([^"]*)" y \
en el campo password "([^"]*)"')
def dado_que_tecleo_el_usuario_y_el_password(step, usuario, password):
    iniciar_driver()
    login(usuario, password)


@step(u'cuando presiono el botón Ingresar')
def cuando_presiono_el_boton_ingresar(step):
    world.driver.find_element_by_xpath("//button[@type='submit']").click()


@step(u'entonces puedo ver la barra de menú principal del sistema')
def entonces_puedo_ver_la_barra_de_menu_principal_del_sistema(step):
    assert is_element_present(By.XPATH, "//div[@id='wrapper']/nav"), \
        "No se encuentra el elemento"


@step(u'entonces puedo ver mensaje "([^"]*)" y \
vuelve a la pantalla de ingreso')
def entonces_puedo_ver_mensaje_y_vuelve_a_pantalla_de_ingreso(step, mensaje):
    time.sleep(3)
    resultado = world.driver.find_element_by_tag_name("h2")
    assert resultado.text == mensaje, \
        'No coinciden los mensajes ' + resultado.text + " y " + mensaje
    time.sleep(3)
    assert is_element_present(By.ID, "login"), \
        "No se encuentra el elemento"


'''
--------------------------------------------------------------------------------
Inicia pruebas de registro
--------------------------------------------------------------------------------
'''

'''
--------------------------------------------------------------------------------
Helpers
--------------------------------------------------------------------------------
'''


def is_element_present(how, what):
    try:
        world.driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def login(usuario, password):
    world.driver.get(
        "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login")
    world.driver.find_element_by_id("id").clear()
    world.driver.find_element_by_id("id").send_keys(usuario)
    world.driver.find_element_by_id("pass").clear()
    world.driver.find_element_by_id("pass").send_keys(password)


def iniciar_driver():
    if not hasattr(world, 'driver'):
        # world.driver = webdriver.Chrome("chromedriver")
        world.driver = webdriver.Firefox()
    else:
        world.driver.get(
            "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login&accion=logout")
    world.driver.implicitly_wait(1)


def finalizar_driver():
    world.driver.get(
        "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login&accion=logout")
    world.driver.quit()
