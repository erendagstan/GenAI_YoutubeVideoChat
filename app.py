import streamlit as st
import raghelper
import videohelper

if "current_video_url" not in st.session_state:
    st.session_state.current_video_url = None
    st.session_state.current_transcript_docs = []
    st.session_state.videos = []

st.set_page_config(page_title="VidChat: Chat with Youtube Video", layout="centered")
st.image(image="./imgs/app_banner.png")
st.title("VidChat: Chat with Youtube 🤖")
st.divider()

tab_url, tab_search = st.tabs(["URL", "Youtube Search"])

with tab_url:
    video_url = st.text_input("Enter the Youtube URL:", key="url_video_url")
    prompt = st.text_input("Enter the question:", key="url_prompt")
    submit_btn = st.button("ASK", key="url_submit")

    if submit_btn:
        st.video(video_url)
        st.divider()
        if st.session_state.current_video_url != video_url:
            with st.spinner(text="Step 1: Video text is being prepared..."):
                video_transcript_docs = videohelper.get_video_transcript(url=video_url)
                st.session_state.current_transcript_docs = video_transcript_docs
        st.success("The video transcript is cached.")
        st.divider()
        st.session_state.current_video_url = video_url

        with st.spinner(text="Step 2: Answering... Please wait..."):
            ai_response, relevant_docs = raghelper.rag_with_video_transcript(transcripted_docs=st.session_state.current_transcript_docs, prompt=prompt)

        st.info("Answer:")
        st.markdown(ai_response)
        st.divider()

        for doc in relevant_docs:
            st.warning("Reference:")
            st.caption(doc.page_content)
            st.markdown(f"Source: {doc.metadata}")
            st.divider()


with tab_search:
    col_left, col_center, col_right = st.columns([20, 1, 20])

    with col_left:
        st.subheader("Youtube Video Searching")
        st.divider()
        search_term = st.text_input(label="Enter the words you want to search:",key="search_term")
        video_count = st.slider(label="Enter the number of videos:", min_value=1, max_value=5, value=5, key="search_video_count")
        sorting_options = ["Relevance", "Upload Date", "View Count", "Rating"]
        sorting_criteria = st.selectbox(label="Sort by:", options=sorting_options)
        search_btn = st.button(label="Search Video", key="search_btn")
        st.divider()

        if search_btn:
            st.session_state.videos = []
            yt_video_list = videohelper.get_videos_for_search_term(search_term=search_term, video_count=video_count, sorting_criteria=sorting_criteria) # return list
            for video in yt_video_list:
                st.session_state.videos.append(video)

        video_urls = []
        video_titles = {}
        for video in st.session_state.videos:
            video_urls.append(video.video_url)
            video_titles.update({video.video_url: video.video_title})

        selected_video = st.selectbox(
            label="Enter the video that you want to chat with it.",
            options=video_urls,
            format_func=lambda url: video_titles[url],
            key="search_selectbox"
        )

        if selected_video:
            search_prompt = st.text_input(label="Enter your question:", key="search_prompt")
            search_ask_btn = st.button("ASK", key="search_ask_btn")
            st.caption("Selected video:")
            st.video(data=selected_video)
            st.divider()

            if search_ask_btn:
                if st.session_state.current_video_url != selected_video:
                    with st.spinner(text="Step 1: Video text is being prepared..."):
                        video_transcript_docs = videohelper.get_video_transcript(url=selected_video)
                        st.session_state.current_transcript_docs = video_transcript_docs
                    st.success("The video transcript is cached.")
                    st.divider()
                    st.session_state.current_video_url = video_url

                with st.spinner(text="Step 2: Answering... Please wait..."):
                    ai_response, relevant_docs = raghelper.rag_with_video_transcript(
                        transcripted_docs=st.session_state.current_transcript_docs, prompt=search_prompt)

                st.info("Answer:")
                st.markdown(ai_response)
                st.divider()

                for doc in relevant_docs:
                    st.warning("Reference:")
                    st.caption(doc.page_content)
                    st.markdown(f"Source: {doc.metadata}")
                    st.divider()

    with col_center:
        st.empty()

    with col_right:

        st.subheader("Related Videos")
        st.divider()

        for i, video in enumerate(st.session_state.videos):
            st.info(f"Video No: {i + 1}")
            st.video(data=video.video_url)
            st.caption(f"Video Title: {video.video_title}")
            st.caption(f"Channel: {video.channel_name}")
            st.caption(f"Video Duration: {video.duration}")
            st.divider()



