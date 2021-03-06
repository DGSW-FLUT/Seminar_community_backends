import graphene

from seminar.models import PostOfFreeSeminar, PostOfRecruitSeminar, PostOfRequestSeminar, Link


class SearchOfCategory(graphene.ObjectType):
    title = graphene.String()
    namespace = graphene.String()
    username = graphene.String()
    uuid = graphene.UUID()
    id = graphene.Int()
    created_at = graphene.DateTime()
    tag_kind = graphene.String()
    content = graphene.String()
    vote_count = graphene.Int()

    class Meta:
        model = Link


class SearchOfCategoryQuery(graphene.ObjectType):
    search = graphene.List(SearchOfCategory, keyword=graphene.String())

    def resolve_search(self, info, **kwargs):
        keyword = kwargs['keyword']
        result = []
        sentence = ''
        tags = ''
        mention = ''
        for word in keyword.split():
            if word.startswith('$'):
                tags += word[1:]
            elif word.startswith('@'):
                mention += word[1:]
            else:
                if len(sentence) > 0:
                    sentence += ' '
                sentence += word

        for post in PostOfFreeSeminar.objects.filter(title__contains=sentence):
            if tags == "":
                if mention in str(post.link.writer):
                    result.append(SearchOfCategory(
                        title=post.title,
                        created_at=post.created_at,
                        content=post.content,
                        uuid=post.link.uuid,
                        namespace=post.link.namespace,
                        id=post.id,
                        username=post.link.writer,
                        vote_count=post.link
                    ))

        for post in PostOfRequestSeminar.objects.filter(title__contains=sentence):
            if tags in post.tag_kind:
                if mention in str(post.link.writer):
                    result.append(SearchOfCategory(
                        title=post.title,
                        created_at=post.created_at,
                        content=post.content,
                        uuid=post.link.uuid,
                        namespace=post.link.namespace,
                        id=post.id,
                        tag_kind=post.tag_kind,
                        username=post.link.writer
                    ))

        for post in PostOfRecruitSeminar.objects.filter(title__contains=sentence):
            if tags in post.tag_kind:
                if mention in str(post.link.writer):
                    result.append(SearchOfCategory(
                        title=post.title,
                        created_at=post.created_at,
                        content=post.content,
                        uuid=post.link.uuid,
                        namespace=post.link.namespace,
                        id=post.id,
                        tag_kind=post.tag_kind,
                        username=post.link.writer
                    ))

        return result
