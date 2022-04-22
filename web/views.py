from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .models import News, Gallery
from web.forms import FeedbackForm, VacancyForm




def index(request):
    title = 'АО "ПРОМСТРОЙСЕРВИС"'
    description = 'Оффициальный сайт группы компаний ПРОМСТРОЙСЕРВИС'
    return render(request, 'index.html', {'title': title, 'description': description})


def about(request):
    title = 'О нас'
    description = 'Информация о группе компаний ПРОМСТРОЙСЕРВИС'
    return render(request, 'about.html', {'title': title, 'description': description})


def services(request):
    title = 'Услуги'
    description = 'Строительные услуги по всей России. Государственные объекты и объекты других сфер.'
    return render(request, 'services.html', {'title': title, 'description': description})


def news_list(request):
    title = 'Новости компании'
    description = 'Лента новостей группы компаний ПРОМСТРОЙСЕРВИС. Новости строительства'
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'title': title, 'description': description, 'news_list': news_list,
                                              'paginator': paginator, 'page_obj': page_obj})


def news(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    title = news.title
    description = news.text
    return render(request, 'news.html', {'title': title, 'description': description, 'news': news})


def projects(request):
    title = 'Наши проекты'
    description = 'Выполненные проекты в сфере строительства, группой компаний ПРОМСТРОЙСЕРВИС'
    return render(request, 'projects.html', {'title': title, 'description': description})


def gos(request):
    title = 'Государственные объекты'
    description = 'Полный спектр работ по проектированию зданий и сооружений государственного назначения'
    images_skolkovo = Gallery.objects.filter(category='7')
    images_infra = Gallery.objects.filter(category='8')
    images_c_bank = Gallery.objects.filter(category='9')
    images_admin = Gallery.objects.filter(category='10')
    images_gos = Gallery.objects.filter(category='11')
    return render(request, 'gos.html', {'title': title, 'description': description, 'images_skolkovo': images_skolkovo,
                                        'images_infra': images_infra, 'images_c_bank': images_c_bank,
                                        'images_admin': images_admin, 'images_gos': images_gos})


def infra(request):
    title = 'Инфраструктурное строительство'
    description = 'Большой и успешный опыт строительства инженерных сетей и коммуникаций, в том числе и на объектах ' \
                  'Федерального значения.'
    images_infra = Gallery.objects.filter(category='4')
    return render(request, 'infra.html', {'title': title, 'description': description, 'images_infra': images_infra})


def prom(request):
    title = 'Промышленное строительство'
    description = 'Результаты успешного строительства промышленных объектов'
    images_prom = Gallery.objects.filter(category='2')
    return render(request, 'prom.html', {'title': title, 'description': description, 'images_prom': images_prom})


def jil(request):
    title = 'Жилое строительство'
    description = 'Строительство качественного, удобного, недорогого жилья и созданием всех условий для максимально' \
                  ' комфортного проживания.'
    images_jil_1 = Gallery.objects.filter(category='12')
    images_jil_2 = Gallery.objects.filter(category='13')
    images_jil_3 = Gallery.objects.filter(category='14')
    return render(request, 'jil.html', {'title': title, 'description': description, 'images_jil_1': images_jil_1,
                                        'images_jil_2': images_jil_2, 'images_jil_3': images_jil_3})


def torg(request):
    title = 'торгово-коммерческое строительство'
    description = 'Строительство торгово-коммерческих комплексов'
    images_torg = Gallery.objects.filter(category='5')
    return render(request, 'torg.html', {'title': title, 'description': description, 'images_torg': images_torg})


def admin(request):
    title = 'Административные здания'
    description = 'Строительство административных зданий и комплексов'
    images_admin = Gallery.objects.filter(category='6')
    return render(request, 'admin.html', {'title': title, 'description': description, 'images_admin': images_admin})


def vacancies(request):
    title = 'Работать с нами'
    description = ''

    if request.method == 'POST':
        vback = VacancyForm(request.POST, request.FILES)

        if vback.is_valid():
            Vacancy = vback.save(commit=False)
            Vacancy.save()

            return redirect('/')

    else:
        vback = VacancyForm()
    return render(request, 'vacancies.html', {'title': title, 'description': description, 'vback': vback})


def contact(request):
    title = 'Контакты'
    description = ''

    if request.method == 'POST':
        fback = FeedbackForm(request.POST)

        if fback.is_valid():
            Feedback = fback.save(commit=False)
            cd = fback.cleaned_data
            Feedback.save()
            subject = 'Сообщение от {} ({})'.format(cd['name'], cd['email'])
            message = '"{}". {} | {} | {}'.format(cd['text'], cd['name'], cd['phone'], cd['site'])
            send_mail(subject, message, 'site@aopss.ru', [cd['email'], 'mfalcon@mail.ru'])

            return redirect('/')

            secret_key = settings.RECAPTCHA_SECRET_KEY

            # captcha verification
            data = {
                'response': data.get('g-recaptcha-response'),
                'secret': secret_key
            }
            resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result_json = resp.json()

            print(result_json)

            if not result_json.get('success'):
                return render(request, 'contact.html', {'is_robot': True})

    else:
        fback = FeedbackForm()

    return render(request, 'contact.html', {'title': title, 'description': description, 'fback': fback,
                                            'site_key': settings.RECAPTCHA_SITE_KEY})

