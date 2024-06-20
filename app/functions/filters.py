def get_route_with_topic_filter_query_params(topics):
    if topics[0] == '':
        return '/more'
    else:
        topic_strings = map(lambda topic: f'topic={topic}', topics)
        return '/more?' + ('&').join(topic_strings)