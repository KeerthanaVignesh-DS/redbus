from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time



# Set up the WebDriver (e.g., using ChromeDriver)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Open the target website
driver.get('https://www.redbus.in/')
# driver.maximize_window()
wait = WebDriverWait(driver, 100)
actions = ActionChains(driver)
rtc_data = []


# Locate and click the initial element (change the selector to match your needs)
initial_element = driver.find_elements(By.CLASS_NAME, 'rtcBack')
for index in range(len(initial_element)):
    try:
        rtc_name = initial_element[index].find_element(By.CSS_SELECTOR, 'div.rtcName').text
        rating = initial_element[index].find_element(By.CSS_SELECTOR, 'div.lh-18.rating > span').text
        service_count = initial_element[index].find_element(By.CSS_SELECTOR, 'div.serviceCnt').text
        logo_url = initial_element[index].find_element(By.CSS_SELECTOR, 'img.rtcLogo').get_attribute('src')
        official_partner_text = initial_element[index].find_element(By.CSS_SELECTOR, 'div.rtcTrustMaker').text
        actions.move_to_element(initial_element[index]).perform()
        initial_element[index].click()
        # Wait for the new elements to appear (change the selector to match the new elements)
        
        new_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'route_link')))
        route_link = driver.current_url
        # Extract and print values from each new element
        for element in new_elements:
            # Get text content
            text_content = element.text
            route_details = element.find_element(By.CSS_SELECTOR, 'div.route_details').text
            route_details_div = element.find_element(By.CSS_SELECTOR, 'div.route_details')
            route_title = route_details_div.find_element(By.CSS_SELECTOR, 'a.route').get_attribute('title')
            fare = element.find_element(By.CSS_SELECTOR, 'div.route_details p span.fare').text
            total_routes = element.find_element(By.CSS_SELECTOR, 'div.row2 span.totalRoutes').text
            
            try:
                book_now_span = element.find_elements(By.CSS_SELECTOR, 'span.book_now')
                for indexbook in range(len(book_now_span)):
                    # print(f"liElement : {book_now_span[indexbook]}")
                    driver.execute_script("arguments[0].scrollIntoView(true);", book_now_span[indexbook])
                    driver.execute_script("arguments[0].click();", book_now_span[indexbook])
                    time.sleep(2)  # Wait for the calendar to appear
                    calendar_element = element.find_elements(By.CSS_SELECTOR, 'div#calendar30 span.calwid__day.today')
                    driver.execute_script("arguments[0].scrollIntoView(true);", calendar_element[indexbook])
                    driver.execute_script("arguments[0].click();", calendar_element[indexbook])
                    time.sleep(2)  # Wait for the calendar to appear

                    li_element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.bus-item-details')))
                    for liIndex in range(len(li_element)):
                        travels = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.travels').text
                        bus_type = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.bus-type').text
                        departure_time = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.dp-time').text
                        departure_location = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.dp-loc').get_attribute('title')
                        duration = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.dur').text
                        arrival_time = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.bp-time').text
                        arrival_location = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.bp-loc').get_attribute('title')
                        rating = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.rating span').text
                        fare = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.fare span').text
                        seats_available = li_element[liIndex].find_element(By.CSS_SELECTOR, 'div.seat-left').text.split()[0]
                
                        bus_data = {
                            'route_name': route_title,
                            'route_link': route_link,
                            'busname': travels,
                            'bustype': bus_type,
                            'departing_time': departure_time,
                            'duration': duration,
                            'reaching_time': arrival_time,
                            'star_rating': rating,
                            'price': fare,
                            'seats_available': seats_available,
                        }
                        print(f"busdata:{bus_data}")
                        rtc_data.append(bus_data)
            except Exception as cal_error:
                print(f"Calendar interaction error: {cal_error}")
            
                
    except Exception as e:
    
        driver.back()
        
    
        
    driver.get('https://www.redbus.in/')
            # Wait for the carousel to be visible again
    initial_element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rtcBack')))
    df = pd.DataFrame(rtc_data)

    
    # Save to CSV file
    df.to_csv('rtc_details.csv', index=False)



# Close the WebDriver

driver.quit()
