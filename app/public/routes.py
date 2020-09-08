"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

import logging

from flask import abort, render_template, redirect, url_for, request, current_app
from flask_login import current_user

from app.models import Post, Comment
from . import public_bp
from .forms import CommentForm
import os

import face_recognition
import cv2
from flask import send_from_directory

# load numpy array from npy file
from numpy import loadtxt

from app.auth.models import User

from twilio.rest import Client


logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Mostrando los posts del blog')
    page = int(request.args.get('page', 1))
    per_page = 3
    #current_app.config['ITEMS_PER_PAGE']
    post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/index.html", post_pagination=post_pagination)


@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if not post:
        logger.info(f'El post {slug} no existe')
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id,
                          user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route('/media/posts/<filename>')
def media_posts(filename):
    dir_path = os.path.join(
        current_app.config['MEDIA_DIR'],
        current_app.config['POSTS_IMAGES_DIR'])
    return send_from_directory(dir_path, filename)


@public_bp.route("/face/")
def face_user():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    # video_capture = cv2.VideoCapture("https://192.168.1.81:8080/video")
    # Load a sample picture and learn how to recognize it.
    known_face_encodings = load_encoding_image()

    # Create arrays of known face encodings and their names
    contrato_user = current_user.contrato
    users = User.get_by_contrato(contrato_user)
    known_face_names = []
    for user in users:
        known_face_names.append(user.name)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


# Load vector encoding face from CSV file
def load_encoding_image():
    list_csv = []
    contrato_user = current_user.contrato
    cant_user = User.get_by_count(contrato_user)
    users = User.get_by_contrato(contrato_user)
    encoding_dir = current_app.config['CSV_DIR']
    for user in users:
        file_path = os.path.join(encoding_dir, user.csv_name)
        data = loadtxt(file_path)
        list_csv.append(data)

    return list_csv


def send_message():
    account_sid = 'ACdaab67b6d9dce286299fdfec29f310c6'
    auth_token = '0bf0f86d49c16a8596e1c917fa6b56d2'
    client = Client(account_sid, auth_token)
    to_whatsappp_number = '+56931284614'
    from_whatsapp_number = '+18599037783'
    mensaje = client.messages.create(body='Hemos detectado una persona que no se encuentra en nuestra BD', from_=from_whatsapp_number, to=to_whatsappp_number)
