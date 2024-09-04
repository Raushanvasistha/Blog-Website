from django.shortcuts import render, redirect, get_object_or_404
from blogsapp.models import Blog, Comments
from blogsapp.serializers import blogSerializers, commentsSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def BlogsapiView(request,pk=0):         
    
    if request.method == 'GET':     #to get individual blogs and all blogs also
        if pk is not None:
            try:
                blog = Blog.objects.get(id=pk)
                blog_data = blogSerializers(blog)
                return JsonResponse(blog_data.data, safe=False)
            except Blog.DoesNotExist:
                return JsonResponse({'error': 'Post not found'}, status=404)
        else:
            blogsdata = Blog.objects.all()
            new_data = blogSerializers(blogsdata, many=True)
            return JsonResponse(new_data.data, safe=False)    

    elif request.method =='POST':       #to post blogs
        blog = JSONParser().parse(request)
        blog_serializer = blogSerializers(data=blog)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("record Added sucessfully", safe= False)

    elif request.method == 'PUT':       #to update blogs
        blog = JSONParser().parse(request)
        blogsdata= Blog.objects.get(id=blog['id'])
        blog_serializer = blogSerializers(blogsdata, data=blog)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("record updated sucessfully", safe= False)
        
    elif request.method == 'DELETE':        #to delete comments
        blogsdata= Blog.objects.get(pk=pk)
        blogsdata.delete()
        return JsonResponse("record deleted sucessfully", safe= False)



@csrf_exempt
def CommentsapiView(request, id=None):
    def error_response(message, status_code):
        return JsonResponse({'error': message}, status=status_code)

    if request.method == 'GET':     #to get comments by post id
        if id:
            try:
                comment = Comments.objects.get(pk=id)
                comment_data = commentsSerializers(comment)
                return JsonResponse(comment_data.data, safe=False)
            except Comments.DoesNotExist:
                return error_response('Comment not found', 404)
        else:
            post_id = request.GET.get('post_id', None)
            if post_id:
                try:
                    commentsdata = Comments.objects.filter(post_id__bid=post_id)
                except Blog.DoesNotExist:
                    return error_response('Blog not found', 404)
                new_data = commentsSerializers(commentsdata, many=True)
                return JsonResponse(new_data.data, safe=False)
            else:
                return error_response('Post ID not provided', 400)

    elif request.method == 'POST':      #post comments
        comment = JSONParser().parse(request)
        post_id = comment.get('post_id')
        if not post_id:
            return error_response('Post ID not provided', 400)

        try:
            Blog.objects.get(bid=post_id)
        except Blog.DoesNotExist:
            return error_response('Blog not found', 404)

        comment_serializer = commentsSerializers(data=comment)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=201)  # Created
        return JsonResponse(comment_serializer.errors, status=400)  # Bad Request

    elif request.method == 'PUT':       #to update comments
        comment_data = JSONParser().parse(request)
        try:
            comment_instance = Comments.objects.get(pk=comment_data['id'])
        except Comments.DoesNotExist:
            return error_response('Comment not found', 404)

        comment_serializer = commentsSerializers(comment_instance, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=200)  # OK
        return JsonResponse(comment_serializer.errors, status=400)  # Bad Request

    elif request.method == 'DELETE':        #to delete comments
        try:
            comment_instance = Comments.objects.get(pk=id)
            comment_instance.delete()
            return JsonResponse({'message': 'Comment deleted successfully'}, status=204)  # No Content
        except Comments.DoesNotExist:
            return error_response('Comment not found', 404)

    return error_response('Method not allowed', 405)  # Method Not Allowed













