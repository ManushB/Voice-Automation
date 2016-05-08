# -*- coding: utf-8 -*-
import abc
import tempfile
import wave
import mad
from . import paths
from . import vocabcompiler
from . import audioengine
from . import i18n


class GenericPlugin(object):
    def __init__(self, info, config):
        self._plugin_config = config
        self._plugin_info = info

    @property
    def profile(self):
        # FIXME: Remove this in favor of something better
        return self._plugin_config

    @property
    def info(self):
        return self._plugin_info


class SpeechHandlerPlugin(GenericPlugin, i18n.GettextMixin):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        GenericPlugin.__init__(self, *args, **kwargs)
        i18n.GettextMixin.__init__(
            self, self.info.translations, self.profile)

    @abc.abstractmethod
    def get_phrases(self):
        pass

    @abc.abstractmethod
    def handle(self, text, mic):
        pass

    @abc.abstractmethod
    def is_valid(self, text):
        pass

    def get_priority(self):
        return 0


