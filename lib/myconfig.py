import os


class MyConfig:
    ''' My Configuration '''

    m_current_epoch = { 'SegmentEpoch': 1, \
                            'GenerateEpoch': 2, \
                            'EstimateEpoch': 3, \
                            'PruneEpoch': 4, \
                            'EvaluateEpoch': 5 \
                        }

    def getSegmentEpoch(self):
        return m_current_epoch['SegmentEpoch']

    def getGenerateEpoch(self):
        return m_current_epoch['GenerateEpoch']

    def getEstimateEpoch(self):
        return m_current_epoch['EstimateEpoch']

    def getPruneEpoch(self):
        return m_current_epoch['PruneEpoch']

    def getEvaluateEpoch(self):
        return m_current_epoch['EvaluateEpoch']

    m_trainer_dir = '/media/data/Program/trainer'

    def getBaseDir(self):
        return m_trainer_dir

    def getTextDir(self):
        return m_trainer_dir + os.sep + 'texts'

    def getModelDir(self):
        return m_trainer_dir + os.sep + 'models'

    def getFinalModelDir(self):
        return m_trainer_dir + os.sep + 'finals'

    #about 1,200 Chinese characters
    m_minimum_chinese_characters = 1,200
    m_minimum_file_size = m_minimum_chinese_characters * 3 + \
        m_minimum_chinese_characters / 2

    def getMinimumFileSize(self):
        return m_minimum_file_size

    m_segment_postfix = '.segmented'

    def getSegmentPostfix(self):
        return m_segment_postfix

    #For both index page, item page and binary model file
    m_status_postfix = '.status'

    def getStatusPostfix(self):
        return m_status_postfix
