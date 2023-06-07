#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

from flask import Flask,request
from flask_restful import Resource, Api, abort
from urllib import request, parse
app = Flask(__name__)
api = Api(app)
play_courses = {}
class PostPlayCourse(Resource):
    def post(self,course_id):
        print(course_id,request.args.get('course_name'))
        if course_id not in play_courses.keys():
            play_courses[course_id] = request.form['course_name']
            return {course_id : play_courses[course_id]}
        abort(404,message="Course id {} is already present".format(course_id))
api.add_resource(PostPlayCourse,'/Courses/<int:course_id>')

play_courses_get = {1:"Artificial Intelligence",3:"Flask Tutorial",2:"AWS Basics"}
class GetPlayCourse(Resource):
    def get(self,course_id = None):
        if course_id == None:
            return play_courses_get
        elif course_id in play_courses_get:
            return {course_id : play_courses_get[course_id]}
        else:
            abort(404,message="Requested course is not present")
api.add_resource(GetPlayCourse,'/course/<int:course_id>','/course')

class DeletePlayCourses(Resource):
    def delete(self, course_id):
        if course_id in play_courses:
            response_string = '{} course is deleted'.format(play_courses[course_id])
            del play_courses[course_id]
            return response_string
        abort(404, message="Course_Id {} doesn't exist".format(course_id))
api.add_resource(DeletePlayCourses,'/Courses/<int:course_id>')

#Now let's add put method, used to edit contents of an existing resource.
class PlayCourses(Resource):
    def put(self, course_id):
        if course_id not in play_courses:
            abort(404, message="Course_Id {} doesn't exist".format(course_id))
    
        play_courses[course_id] = request.form['course_name']
        return {course_id: play_courses[course_id]}

import requests



if __name__ == "__main__":
    app.run(debug=True)
    