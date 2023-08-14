import time
from tests.conftest import main_page
from tests.conftest import podcaster


def test_deleting_author(authorization):
    main_page.header_drop_button()
    main_page.to_cabinet_button()
    podcaster.click_creating_author()
    podcaster.upload_image('img/Mona_Lisa1.jpg')
    podcaster.fill_author_name('AQA Тест 123')
    podcaster.fill_author_description('По своей сути рыбатекст является альтернативой традиционному '
                                      'lorem ipsum, который вызывает у некторых людей недоумение при '
                                      'попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба '
                                      'на русском языке наполнит любой макет непонятным смыслом и придаст '
                                      'неповторимый колорит советских времен. '
                                      'Вы можете добавить в данное  поле до 600 символов!')
    podcaster.additional_about_author()
    podcaster.fill_additional_email('yksyp@mailto.plus')
    podcaster.fill_additional_phone('88005553535')
    podcaster.submit_button()
    time.sleep(2)
    podcaster.author_settings()
    podcaster.delete_author()
    time.sleep(10)