def groupValidation(request):
    try:
        data = request.POST
        error_message = []
        group_name = data.get('group_name')

        if not group_name:
            error_message.append("Group name can be null.")

        return error_message, group_name
    except Exception as exe:
        raise Exception(exe)
