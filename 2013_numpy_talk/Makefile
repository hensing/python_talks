INTERFACE= $(shell netstat -nr | grep default | cut -d 'e' -f 3)
MYIP= $(shell ifconfig e$(INTERFACE) | grep "inet " |cut -d ' ' -f 2)

all: convert upload

convert:
	ipython nbconvert --to slides numpy_talk.ipynb

upload:
	scp numpy_talk.slides.html cleo:code/pyBonn/numpy_talk/
	rsync -avuL ./ dickten.info:dickten.info/numpy_talk/

notebook:
	ipython notebook --pylab inline

server:
	ipython notebook --pylab inline --ip=$(MYIP)
