import json
import logging
from rest_framework import serializers
from ussd.core import UssdView
from .models import Survey, SurveyResult
from .helpers import read_journey, validate_ussd_journey, get_survey_endpoint_and_id

logger = logging.getLogger(__name__)

def validate_yaml(value):

    try:
        journey = read_journey(value['journeys'])
        is_valid, errors = UssdView.validate_ussd_journey(journey)

        # validate the existance and form of a custom defined initialize_survey screen
        if is_valid:
            is_valid, errors = validate_ussd_journey(journey)
    except Exception as ex:
        logger.error(ex)
        raise serializers.ValidationError({"journeys":["The yaml file is invalid."]})

    if(not(is_valid)):
        raise serializers.ValidationError({"journeys":[json.dumps(errors)]})

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id','survey_id', 'title', 'published', 'endpoint', 'journeys')
        validators = [ validate_yaml ]
        
    def to_internal_value(self, data):
        # assign endpoint and survey_id by reading from the uploaded file
        # TODO:
        # find a better way not to revalidate the yaml file again
        try:
            journey = read_journey(data['journeys'])
            is_valid, errors = UssdView.validate_ussd_journey(journey)

            if is_valid:
                is_valid, errors = validate_ussd_journey(journey)
            if is_valid:
                d = get_survey_endpoint_and_id(journey)
                data['endpoint'] = d['endpoint']
                data['survey_id'] = d['survey_id']
        except Exception as ex:
            logger.error(ex)

        return super(SurveySerializer,self).to_internal_value(data)


class SurveyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResult
        fields = ('id','survey','subscriber', 'result')