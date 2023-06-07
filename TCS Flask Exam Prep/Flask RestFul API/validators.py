def validate(request):
    if(request.form == {}):
        return ["False",""]
    name = request.form.get('name')
    if(len(name) <=8 or len(name) >=15):
        return ["False","name"]
    mobile =request.form.get('mobile')
    mobile = str(mobile)
    if(len(mobile) != 10):
        return ["False","mobile"]
    else:
        start = mobile[0]
        if start not in ['6','7','8','9']:
            return ["False",'mobile']
    return ['True']