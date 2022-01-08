from os import stat
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

class scraper():
    #Runs without browser
    global chrome_options
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    def anime_scrape(self, url, driver_path):
        
        #Puts chromedriver path as function parameter and runs chrome with specified options
        driver = webdriver.Chrome(driver_path, options=chrome_options)

        #Running the function's url parameter
        
        #Used for more data
        anime_links = []
        
        
        names_list = []
        img_links = []
        desc_list = []
        status_list = []
        genre_list = []
        released_list = []
        total_episodes = []
        episode_links = []
        slug_list = []
        episode_iframe_array = []
            
        for e in ['special','A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']:
            driver.get(url + str(e))
            
            time.sleep(5)
        
            urls_list = []
            print(e)
            
            names = driver.find_elements_by_class_name('name')
            for name in names:
                names_list.append(name.text)
            
            time.sleep(3)
                
            names_list.pop(74)
            for i in range(1,75):
                link = driver.find_element_by_xpath('//*[@id="wrapper_bg"]/div[1]/div[1]/div/div/ul/li[' + str(i) + ']/a').get_attribute('href')
                anime_links.append(link)
            time.sleep(3)
                #print(link)
            
            for link in anime_links:
                driver.get(link)
                desc = driver.find_element_by_css_selector('#wrapper_bg > div.content > div.content_left > div > div > div.right > p:nth-child(5)').text
                desc_list.append(desc)
                temp_link = link.split('.html')[0]
                slug = temp_link.split('https://animeseries.so/anime/')[1]
                slug_list.append(slug)
                
                img = driver.find_element_by_class_name('img-responsive').get_attribute('src')
                img_links.append(img)
                
                time.sleep(3)
                   
                status = driver.find_element_by_xpath('//*[@id="wrapper_bg"]/div[1]/div[1]/div/div/div[2]/p[4]/a').get_attribute('title')
                status_list.append(status)
                
                time.sleep(3)
                
                released = driver.find_element_by_xpath('//*[@id="wrapper_bg"]/div[1]/div[1]/div/div/div[2]/p[5]/a').get_attribute('title')
                released_list.append(released)
                
                time.sleep(3)
                
                genres = driver.find_elements_by_class_name('des')[4]
                genre_list.append(genres.text)
                
                time.sleep(3)

                try:
                    episode = driver.find_element_by_class_name('name').text
                    total_episodes.append(episode)
                except NoSuchElementException:
                    total_episodes.append("None")
                
                episode_link = driver.find_element_by_xpath('//*[@id="wrapper_bg"]/div[1]/div[1]/div/div/div[7]/ul/li/a').get_attribute('href')
                episode_links.append(episode_link)
                
                time.sleep(3)
                
                
                
            for link in episode_links:
                
                
                driver.get(link)
                #driver.get(link)
                elements = driver.execute_script("a = $('.row > .right > a'); urls = []; for(var i =0; i < a.length; i++){urls.push(a[i].getAttribute('data-video'));} return urls")
                episode_iframe_array.append(elements)
        
        
        
        '''
        print(len(names_list))
        print(len(img_links))
        print(len(desc_list))
        print(len(status_list))
        print(len(genre_list))
        print(len(slug_list))
        print(len(released_list))
        print(len(total_episodes))
        print(len(episode_links))
        print(len(episode_iframe_array))
        '''
        return names_list, img_links, desc_list, status_list, genre_list, slug_list, released_list, total_episodes, episode_links, episode_iframe_array
