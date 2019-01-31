from django.urls import path

from .views import (
    ListCreateArticle,
    RetrieveUpdateDestroyArticle,
    RetrieveAuthorArticles,
    FavoriteArticlesView,
    UnfavoriteArticleView,
    ListTag,
    LikeArticleAPIView,
    ArticleSearchListAPIView,
    BookmarkArticleView,
    UnBookmarkArticleView,
    GetBookmarkArticle,
    ShareArticleView,
    ReadingStatsView,
    HighlightListCreate,
    DislikeArticleAPIView,
    ReportArticleAPIView
)


app_name = "articles"
urlpatterns = [
    path(
        '',
        ListCreateArticle.as_view(),
        name="articles_list"
    ),
    path(
        '<slug:slug>/',
        RetrieveUpdateDestroyArticle.as_view(),
        name="article_detail"
    ),
    path(
        'author/<int:pk>/',
        RetrieveAuthorArticles.as_view(),
        name="author_articles"
    ),
    path(
        'author/<str:username>/',
        RetrieveAuthorArticles.as_view(),
        name="author_articles"
    ),
    path(
        'tags',
        ListTag.as_view(),
        name="tags_list"
    ),
    path(
        '<slug:slug>/favorite',
        FavoriteArticlesView.as_view(),
        name="favorite-articles"
    ),
    path(
        '<slug:slug>/favorite/<int:pk>/',
        UnfavoriteArticleView.as_view(),
        name="unfavorite-articles"
    ),
    path(
        '<slug:slug>/like',
        LikeArticleAPIView.as_view(),
        name="like-article"
    ),
    path(
        '<slug:slug>/dislike',
        DislikeArticleAPIView.as_view(),
        name="dislike-article"
    ),
    path(
        'search',
        ArticleSearchListAPIView.as_view(),
        name="search-article"
    ),
    path(
        '<slug:slug>/bookmark',
        BookmarkArticleView.as_view(),
        name="bookmark-articles"
    ),
    path(
        '<slug:slug>/bookmark/<int:pk>',
        UnBookmarkArticleView.as_view(),
        name="unbookmark-articles"
    ),
    path(
        'bookmark/<int:pk>',
        GetBookmarkArticle.as_view(),
        name="get-bookmark-articles"
    ),
    path(
        '<slug:slug>/share/<str:provider>/',
        ShareArticleView.as_view(),
        name="share-article"
    ),
    path(
        'stats',
        ReadingStatsView.as_view(),
        name="reading-stats"
    ),
    path(
        '<slug:slug>/highlight',
        HighlightListCreate.as_view(),
        name="article_highlight"
    ),
    path(
        '<slug:slug>/report',
        ReportArticleAPIView.as_view(),
        name='report-article'
    ),
    path(
        'reported',
        ReportArticleAPIView.as_view(),
        name='reported-articles'
    ),
    path(
        'search',
        ArticleSearchListAPIView.as_view(),
        name="search-article"
    )
]
