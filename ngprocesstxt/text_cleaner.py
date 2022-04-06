from text_processing import *


class CleanText:
    """
        This is a pipeline used for cleaning the given
        text input. This pipeline makes use of the methods
        withing text_processing module.
    """

    def __init__(self, input_text):
        self.input_text = input_text

    def cleaning_pipeline(self):
        """
            This function performs multiple text cleaning operations
            and returns the cleaned output text.

            :param self: Inherited from class attributes
            :return: Cleaned output text
            :rtype: str
        """

        try:
            input_text_1 = clean_html(self.input_text)
        except Exception as e:
            raise Exception()

        try:
            input_text_2 = expand_domain_specific_shortforms(
                input_text_1)
        except Exception as e:
            raise Exception()

        try:
            input_text_3 = expand_general_shortforms(input_text_2)
        except Exception as e:
            raise Exception()

        # try:
        #     input_text_4 = remove_name(input_text_3)
        # except Exception as e:
        #     raise Exception()

        # try:
        #     input_text_5 = remove_address(input_text_4)
        # except Exception as e:
        #     raise Exception()

        try:
            input_text_6 = fix_encoding_decoding_errors(input_text_3)
        except Exception as e:
            raise Exception()

        try:
            input_text_7 = remove_bullets(input_text_6)
        except Exception as e:
            raise Exception()

        try:
            input_text_8 = remove_url(input_text_7)
        except Exception as e:
            raise Exception()

        try:
            input_text_9 = replace_hexcodes(input_text_8)
        except Exception as e:
            raise Exception()

        try:
            input_text_10 = remove_contact_number(input_text_9)
        except Exception as e:
            raise Exception()

        try:
            input_text_11 = clean_email_data(input_text_10)
        except Exception as e:
            raise Exception()

        try:
            input_text_12 = clean_socialmedia_tags(input_text_11)
        except Exception as e:
            raise Exception()

        try:
            input_text_13 = fix_contractions(input_text_12)
        except Exception as e:
            raise Exception()

        try:
            input_text_14 = remove_symbols_emojis(input_text_13)
        except Exception as e:
            raise Exception()

        try:
            input_text_15 = replace_punctuations(input_text_14)
        except Exception as e:
            raise Exception()

        try:
            input_text_16 = remove_extra_spaces(input_text_15)
        except Exception as e:
            raise Exception()

        try:
            final_text = fix_spelling(input_text_16)
        except Exception as e:
            raise Exception()

        return final_text
