from django.template.loader import get_template
from django.core.mail import EmailMessage
from shor.email_info import EMAIL_FROM, EMAIL_ADMIN
from django.forms.models import model_to_dict
from landing.models import LetterTemplate, LetterEmail


class SendingEmail(object):
    email_from = "Shor Professional Ukraine <%s>" % EMAIL_FROM
    reply_to_emails = [email_from]
    target_emails = []
    bcc_emails = []

    def sending_email(self, type_id, email=None, order=None, email_details=None):
        if not email:
            email = EMAIL_ADMIN

        target_emails = [email]

        vars = {}

        if type_id == 1:
            name = "Activation"
            print('----после трай --------111111111111')
            print('----после трай-----------11111111111', email_details)
            print('----после трай-----------11111111111', type(email_details))
            print('----после трай-----------11111111111', email_details['user'])

            letter_template = LetterTemplate. objects.get(name=name)
            print(letter_template)
            subject = letter_template.subject
            print(subject)
            message = get_template('landing/acc_confirmation_email.html').render(email_details)
            print(('---------MSG------------', message))
            target_emails = [email_details['to_list']]
            print('---------------отправка----НА--------', target_emails)

            # vars["order_fields"] = model_to_dict(order)
            # vars["order"] = order
        elif type_id == 2:
            name = "Contact_Us_Form"
            try:
                print('----после трай')
                print('----после трай', email_details)
                letter_template = LetterTemplate. objects.get(name=name)
                subject = letter_template.subject
                print(subject)
                message = letter_template.message
                print(message)
                print('--------------11111111111111111111-------------')
                receiver_emails = LetterEmail.objects.filter(letter_template_name=letter_template)
                print('-----------------------', receiver_emails)
                target_emails = []
                for r in receiver_emails:
                    target_emails.append(r.email_receiver)
                print(target_emails)


                # try:
                #     message = get_template('landing/acc_confirmation_email.html').render(vars)
                # except:
                #     message = letter_template.message
                # print('----Это МЕСАГА-----', message)
                # target_emails = [email_details['to_list']]
            except:
                pass

            # vars["order_fields"] = model_to_dict(order)
            # vars["order"] = order
        elif type_id == 3:
            subject = "номер 3"
            message = get_template('landing/acc_confirmation_email.html').render(vars)

        # print('----Это МЕСАГА-----', message)
        print('----Это from-----', self.email_from)
        print('----Это to-----', target_emails, type(target_emails))

        msg = EmailMessage(subject, message, from_email=self.email_from, to=target_emails,
                           bcc=self.bcc_emails, reply_to=self.reply_to_emails)
        msg.content_subtype = 'html'
        msg.mixed_subtype = 'related'
        print('----and here- hre hre hre hre')
        msg.send()

        print('ВЫСЛАНО ПИСЬМО УСПЕШНО')


