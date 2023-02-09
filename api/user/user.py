from flask import Flask, request, abort
#from flask import Flask, request, jsonify

from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('')
class UserManagement(Resource):
    def get(self):
        # GET method 구현 부분
        database=Database()
        data=request.get_json()

        row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %(data['id'], data['pw']))
        database.commit()

        #아이디 비밀번호 일치
        if(row is not None):
            result={'nickname':row['nickname']}
        else:
            row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s';" %data['id'])

            #해당 유저 존재
            if(row is not None):
                result={'message':'아이디나 비밀번호 불일치'}
                return result, 400
            #해당 유저 없음
            else:
                result={'message':'해당 유저가 존재하지 않음'}
                return result, 400

    def post(self):
        # POST method 구현 부분
        database=Database()
        data=request.get_json()
        
        #이미 있는 유저인지 체크
        row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s';" %data['id'])

        #이미 있는 유저
        if(row is not None):
            result={'is_success':False,
                    'message':'이미 있는 유저'}
            return result, 400
        else:
            row=database.execute_one("INSERT INTO SeongHui.user VALUES ('%s','%s','%s');" %(data['id'], data['pw'], data['nickname']))
            result={'is_success':True,
                    'message':'유저 생성 성공'}
            database.commit()
            database.close()
            return result
            
        

    def put(self):
        # PUT method 구현 부분
        database=Database()
        data=request.get_json()

        #있는 유저인지 확인
        row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %(data['id'], data['pw']))
        if (row is not None):
            row=database.execute_one("SELECT * FROM SeongHui.user WHERE nickname = '%s';" %(data['nickname']))
            #현재 닉네임와 같음
            if(row is not None):
                result={'is_success':False,
                    'message':'현재 닉네임과 같음'}
                return result,400
            else:
                database.execute_one("UPDATE SeongHui.user SET nickname='%s' WHERE id = '%s' AND pw = '%s';" %(data['nickname'], data['id'], data['pw']))
                database.commit()
                database.close()
                result={'is_success':True,
                    'message':'유저 닉네임 변경 성공'}
                return result
        
        else:
            result={'is_success':False,
                    'message':'아이디나 비밀번호 불일치'}
            return result,400
    
    def delete(self):
        # DELETE method 구현 부분
        database=Database()
        data=request.get_json()

        #있는 유저인지 확인
        row=database.execute_one("SELECT * FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %(data['id'], data['pw']))

        if (row is not None):
            database.execute_one("DELETE FROM SeongHui.user WHERE id = '%s' AND pw = '%s';" %(data['id'],data['pw']))
            result={'is_success':True,
                    'message':'유저 삭제 성공'}
            database.commit()
            database.close()
            return result
        else:
            result={'is_success':False,
                    'message':'아이디나 비밀번호 불일치'}
            return result, 400
