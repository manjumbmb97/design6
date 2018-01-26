import os

def get_upload_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s%s.%s" % ('img', instance.pk, ext)

	return os.path.join('users', instance.user.username, filename)