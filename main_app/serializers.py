from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Visual, Notes
from rest_framework.validators import UniqueValidator

class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    # token = serializers.CharField(max_length=255, read_only=True)
    def login_view(request):
      # if post, then authenticate (the user will be submitting a username and password)
      print(request)
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
          u = form.cleaned_data['email']
          p = form.cleaned_data.get('password')
          user = authenticate(username=u, password=p)
          if user is not None:
            if user.is_active:
                 login(request, user)
              # return HttpResponseRedirect('/user/' + u)
            else:
                print(f"The account for {u} has been disabled.")
      else:
        print('The username and/or password is incorrect.')
      # else: # get request that sent up empty form
      #   form = AuthenticationForm()
      #   # return render(request, 'login', {'form': form})
      #   return form

    # def validate(self, validated_data):
    #     email = validated_data.get("email", None)
    #     print(email)
    #     password = validated_data.get("password", None)
    #     user = authenticate(email=email, password=password)
    #     if user is None:
    #         raise serializers.ValidationError(
    #             'Username or password is incorrect.'
    #         )
    #     # try:
    #     #     payload = JWT_PAYLOAD_HANDLER(user)
    #     #     jwt_token = JWT_ENCODE_HANDLER(payload)
    #     #     update_last_login(None, user)
    #     if User.DoesNotExist:
    #         raise serializers.ValidationError(
    #             'User with given email and password does not exist'
    #         )
    #     return {
    #         'email': user.email,
    #         'token': jwt_token
    #     }
