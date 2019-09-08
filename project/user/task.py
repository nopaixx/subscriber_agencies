#In this page we can define the task running
#async in celery or we can define our lamda code


# this task is asyncorn by using celery task in develop envorinoment
# or simply you can define this function as a lambda handle
def handle_send_message_user(User, new_topic):
    """
    This endpoint recibe a user and send a user message
    into Provider HUB
    """

    #1.-Get user subcription hub user_provider_hub table Case1

    #2.-For each provider you send a message inside new topic create
    #    you need a class provider can manager all providers

    #3.-Update table history_logging
