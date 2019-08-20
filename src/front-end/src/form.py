from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import InputRequired

# Form ORM
class Form(FlaskForm):
	Model_Name = StringField('Enter the Machine Learning Model Name.', validators=[InputRequired()])
	Version = IntegerField('Enter the Experiment Version Number.', validators=[InputRequired()])
	Dataset_Name = SelectField(
		'Choose the training Dataset Type/Endpoint.',
		validators=[InputRequired()],
		choices=[
			('coco', 'Common Objects in Context'),
			('kitti', 'KITTI Vision Suite'),
			('voc', 'PASCAL Visual Object Classes'),
			('fashion', 'Fashion-MNIST')
		]
	)
	Github_Repo = StringField('Enter the Name of the Training Source Code Repository.', validators=[InputRequired()])
	Github_User = StringField('Enter the User Name for the Training Source Code Repository.', validators=[InputRequired()])
	Platform = SelectField(
		'Choose the Training Cluster Platform.',
		validators=[InputRequired()],
		choices=[
			('sagemaker', 'Amazon SageMaker')
			# ('eks', 'Amazon EKS'),
			# ('dlami', 'Amazon Deep Learning AMI')
		]
	)
	Training_Instance = SelectField(
		'Choose a Training Instance type.',
		validators=[InputRequired()],
		choices=[
			('ml.p2.xlarge', 'ml.p2.xlarge'),
			('ml.p2.8xlarge', 'ml.p2.8xlarge'),
			('ml.p2.16xlarge', 'ml.p2.16xlarge'),
			('ml.p3.2xlarge', 'ml.p3.2xlarge'),
			('ml.p3.8xlarge', 'ml.p3.8xlarge'),
			('ml.p3.16xlarge', 'ml.p3.16xlarge')
		]
	)
	Instance_Count = IntegerField('Enter the number of Training Instances.', validators=[InputRequired()])
	Hyperparameters = StringField('Enter the JSON String of model Hyperparameters.', validators=[InputRequired()])
	submit = SubmitField('Submit')