import base64
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from config.default import config
from src.helpers.utils import get_text, setup, get_file_path, generate_response


def create_app(config_name):
    """Create a streamlit app"""
    cf = config[config_name]
    st.set_page_config(page_title='haidongGPT from pdf',
                       page_icon='🤖', layout='centered', initial_sidebar_state='auto')
    st.header(cf.TITLE)
    # we need a way to remember the chat history
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''
    if 'generated' not in st.session_state:
        st.session_state.generated = []
    if 'past' not in st.session_state:
        st.session_state.past = []
    if 'source' not in st.session_state:
        st.session_state.source = []

    """
    *---------------------------------------*-----------------------------------------------------*
    *---------------------------------------*-----------------------------------------------------*
                                  ****Utility method****
    """
    def submit():
        st.session_state.user_input = st.session_state.widget
        st.session_state.widget = ''

    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width={cf.WIDTH} ' \
                          f'height={cf.HEIGHT} type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    def excerpt(text, n=cf.EXCERPT_LENGTH):
        return text[:n] + '...' if len(text) > n else text
    """
    *---------------------------------------*-----------------------------------------------------*
    *---------------------------------------*-----------------------------------------------------*
    """

    # let the user upload a pdf or txt file
    pdf = st.file_uploader(
        'Upload a PDF file',
        type=[ext for ext in cf.ALLOWED_FILE_EXTENSION.split(',')],
        accept_multiple_files=cf.ALLOW_MULTIPLE_FILES,
        label_visibility='hidden'
    )
    if pdf is not None:
        # show the pdf thumbnail :-)
        fp = get_file_path(pdf)
        show_pdf(fp)
        colored_header(label='', description='', color_name='light-blue-70')
        response_container = st.container()
        # processing start here...
        s = setup(file=fp, number_of_relevant_chunk=cf.NUMBER_OF_RELEVANT_CHUNKS)
        st.text_input('🤖 666 👋🏾, Ask me anything about the uploaded pdf', key='widget', on_change=submit)
        with response_container:
            if st.session_state.user_input:
                response = generate_response(st.session_state.user_input, cf.CHAIN_TYPE, s)
                if response['source_documents']:
                    all_refs = ''
                    for doc in response['source_documents']:
                        content = excerpt(doc.page_content)
                        page = doc.metadata.get('page')
                        ref = f"""
                        *{content}*
                        \n☝🏽#{page} 📖\n
                        """
                        all_refs += ref
                    st.session_state.source.append(all_refs)
                st.session_state.past.append(st.session_state.user_input)
                st.session_state.generated.append(response['result'])
            if st.session_state.generated:
                for i in range(len(st.session_state.generated)):
                    message(st.session_state.past[i], is_user=True, key=str(i) + '_user', avatar_style='micah')
                    message(st.session_state.generated[i], key=str(i))
                    if st.session_state.source:
                        with st.expander(':blue[See references]'):
                            st.markdown(st.session_state.source[i], unsafe_allow_html=True)
