import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple
import datetime
import re

"""
Se supone que hemos entrado ya en la url del restaurante
"""
class Restaurant:
    def __init__(self, driver: webdriver, url_restaurante: str) -> None:
        self.driver: webdriver = driver
        self.url: str = url_restaurante

        self.driver.get(self.url)

    def accept_cookies(self, path_cookie: str) -> None:
        accept_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, path_cookie)))
        accept_button.click()
    def get_title(self) -> str:
        # Pablo
        pass


    def get_address(self) -> str:
        # Edu
        print("Hello")
        pass


    def get_coordinates(self) -> Tuple[str, str]:
        # Anton
        map_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[3]/a'
        map_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, map_path)))
        
        href: str = map_element.get_attribute("href")

        pattern: str = r"(?P<lat>-?[0-9]+\.[0-9]+),(?P<long>-?[0-9]+\.[0-9]+)"  # cuidado: no pusiste r
        coordinates: re.Match = re.search(pattern, href)
        lat: str = coordinates.group("lat")
        long: str = coordinates.group("long")

        return (lat, long)

    def get_total_rating(self) -> int:
        # Edu
        pass


    def get_rating(self) -> int:
        # Edu
        pass


    def get_type_restaurant(self) -> List[str]:
        '''
         # Pablo
        A lo mejor hay que crear funciones auxiliares que filtran los diferentes tipos de restaurantes
        '''
        pass

    def get_bookmarks(self) -> int:
        # Anton
        path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[1]/ul/li[2]/div[3]/span'
        bookmarks = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, path)))
        
        return int(bookmarks.text)



    def get_price_range(self) -> str:
        '''
        # Edu
        Crear una función auxiliar que convierte los iconos dollars a: Cheap, Medium, Expensive (o lo que sea)
        '''
        pass


    def get_telephone_number(self) -> str:
         # Pablo
        pass


    def get_email(self) -> str:
         # Pablo
        pass


    def get_restaurant_website(self) -> str:
        '''
        # Anton
        Hacer un try except por si no existe un sitio web del restaurante
        '''
        pass


    def get_timetable(self) -> Dict[str, str]:
        '''
        # Anton
        Crear un diccionario con clave siendo el día de la semana y el valor el horario ese día
        '''
        view_hours_path: str = "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[2]/div/div/a"
        hours_list_path: str = "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[2]/div/div/ul/li/child::*"

        view_hours_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, view_hours_path)))
        view_hours_button.click()
        time.sleep(0.6)

        timetable: Dict[str, str] = {}
        day = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH,hours_list_path))
        )
        for i in range(len(day) // 2):
            timetable[day[i * 2].text] = day[(i * 2) + 1].text
        return timetable
    