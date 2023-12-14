from rest_framework import serializers
from .models import UserAccount
from xml.dom import ValidationErr
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Utils
class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=255, write_only=True, style={
                                 'input_type': 'password'})
    class Meta:
        model = UserAccount
        fields = ['name','email','password','password2','is_agent']
        extra_kwrgs={'password':{'write_only':True}}
        
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "Password does't match Please Retype Thankyou")
        elif len(password) < 6:
            raise serializers.ValidationError({'msg': 'Password must be at least 6 characters'})
        return attrs
    def create(self, validate_data):
        return UserAccount.objects.create_user(**validate_data )
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,)
    class Meta:
        model= UserAccount
        fields = ['email','password']
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','email','name','is_agent')
class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,write_only=True, style = {'input_type':'password'} )
    password2 = serializers.CharField(max_length=255,write_only=True, style = {'input_type':'password'} )
    class Meta:
        model= UserAccount
        fields=['password','password2']
    def validate(self,attrs):
            password= attrs.get('password')
            password2= attrs.get('password2')
            user = self.context.get('user')
            if password != password2:
                raise serializers.ValidationError("password and confirm password does't match !")
            elif len(password) < 6:
                raise serializers.ValidationError(
                    "Password must be at least 6 characters")
            user.set_password(password)
            user.save()
            return attrs
class PasswordResetSendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length= 255)
    class Meta:
        # model = UserAccount
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if UserAccount.objects.filter(email=email).exists():
            user = UserAccount.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id) )
            print('Encoded Uid :' , uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token :', token)
            link = 'http://localhost:3000/api/user/rest/'+uid+'/'+token
            print( "link password rest :", link)
            body = 'Password Reset Link: ' +' '+ link
            data ={
                'subject':'Reset Your Password: ',
                'body': body,
                'to_email':user.email
            }
            Utils.send_mail(data)
            return attrs
        else:
            raise ValidationErr('Email is Not Found in Database')
class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, write_only=True, style={
                                         'input_type': 'password'})
    password2 = serializers.CharField(max_length=255,write_only=True, style = {'input_type':'password'} )
    class Meta:
        # model= UserAccount
        fields=['password','password2']
    def validate(self,attrs):
            try:
                password = attrs.get('password')
                password2 = attrs.get('password2')
                uid = self.context.get('uid')
                token = self.context.get('token')
                if password != password2:
                    raise serializers.ValidationError(
                        "password and confirm password does't match !")
                elif len(password) < 6:
                    raise serializers.ValidationError(
                        "Password must be at least 6 characters")
                id = smart_str(urlsafe_base64_decode(uid))
                user = UserAccount.objects.get(id=id)
                if not PasswordResetTokenGenerator().check_token(user, token):
                    raise serializers.ValidationError(
                        'Token is Not Valid or Expired')
                user.set_password(password)
                user.save()
                return attrs
            except DjangoUnicodeDecodeError as identifier:
                PasswordResetTokenGenerator().check_token(user, token)
                raise serializers.ValidationError(
                    'Token is Not Valid or Expired')
