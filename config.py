#!/usr/bin/env python3
import urllib.parse, pyodbc
from sqlalchemy import create_engine



params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=.\SQLEXPRESS; Data Source=(LocalDB)\MSSQLLocalDB; DATABASE=dbloteria; User=sa; Pwd=root')
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_timeout=60, echo=True)

SQLALCHEMY_TRACK_MODIFICATIONS = True


SECRET_KEY = "b'&\xf0*p)\xe0i\xa0]'(\xecoX\\x12cb'\xe9\\x96\xec\\x96H\xa6I\xef\\x02\xac\xdaD%\xff\xce\\x93\\(#\xd8\xf8i\xf5\x0f\xef\\x85\xc1\x9a\xd1\xb7\x9ez'"


# SESSION_COOKIE_NAME = 'psa_session'
DEBUG = True

# DEBUG_TB_INTERCEPT_REDIRECTS = False
# SESSION_PROTECTION = 'strong'

# SOCIAL_AUTH_LOGIN_URL = '/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/done/'
# SOCIAL_AUTH_USER_MODEL = 'example.models.user.User'
# SOCIAL_AUTH_STORAGE = 'social_flask_sqlalchemy.models.FlaskStorage'
# SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
#     'social_core.backends.amazon.AmazonOAuth2',
#     'social_core.backends.angel.AngelOAuth2',
#     'social_core.backends.aol.AOLOpenId',
#     'social_core.backends.appsfuel.AppsfuelOAuth2',
#     'social_core.backends.beats.BeatsOAuth2',
#     'social_core.backends.behance.BehanceOAuth2',
#     'social_core.backends.belgiumeid.BelgiumEIDOpenId',
#     'social_core.backends.bitbucket.BitbucketOAuth',
#     'social_core.backends.box.BoxOAuth2',
#     'social_core.backends.clef.ClefOAuth2',
#     'social_core.backends.coinbase.CoinbaseOAuth2',
#     'social_core.backends.coursera.CourseraOAuth2',
#     'social_core.backends.dailymotion.DailymotionOAuth2',
#     'social_core.backends.deezer.DeezerOAuth2',
#     'social_core.backends.disqus.DisqusOAuth2',
#     'social_core.backends.douban.DoubanOAuth2',
#     'social_core.backends.dropbox.DropboxOAuth',
#     'social_core.backends.dropbox.DropboxOAuth2',
#     'social_core.backends.eveonline.EVEOnlineOAuth2',
#     'social_core.backends.evernote.EvernoteSandboxOAuth',
#     'social_core.backends.facebook.FacebookAppOAuth2',
#     'social_core.backends.facebook.FacebookOAuth2',
#     'social_core.backends.fedora.FedoraOpenId',
#     'social_core.backends.fitbit.FitbitOAuth2',
#     'social_core.backends.flickr.FlickrOAuth',
#     'social_core.backends.foursquare.FoursquareOAuth2',
#     'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.google.GoogleOAuth',
#     'social_core.backends.google.GoogleOAuth2',
#     'social_core.backends.google.GoogleOpenId',
#     'social_core.backends.google.GooglePlusAuth',
#     'social_core.backends.google_openidconnect.GoogleOpenIdConnect',
#     'social_core.backends.instagram.InstagramOAuth2',
#     'social_core.backends.jawbone.JawboneOAuth2',
#     'social_core.backends.kakao.KakaoOAuth2',
#     'social_core.backends.linkedin.LinkedinOAuth',
#     'social_core.backends.linkedin.LinkedinOAuth2',
#     'social_core.backends.live.LiveOAuth2',
#     'social_core.backends.livejournal.LiveJournalOpenId',
#     'social_core.backends.mailru.MailruOAuth2',
#     'social_core.backends.mendeley.MendeleyOAuth',
#     'social_core.backends.mendeley.MendeleyOAuth2',
#     'social_core.backends.mineid.MineIDOAuth2',
#     'social_core.backends.mixcloud.MixcloudOAuth2',
#     'social_core.backends.nationbuilder.NationBuilderOAuth2',
#     'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
#     'social_core.backends.open_id.OpenIdAuth',
#     'social_core.backends.openstreetmap.OpenStreetMapOAuth',
#     'social_core.backends.persona.PersonaAuth',
#     'social_core.backends.podio.PodioOAuth2',
#     'social_core.backends.rdio.RdioOAuth1',
#     'social_core.backends.rdio.RdioOAuth2',
#     'social_core.backends.readability.ReadabilityOAuth',
#     'social_core.backends.reddit.RedditOAuth2',
#     'social_core.backends.runkeeper.RunKeeperOAuth2',
#     'social_core.backends.sketchfab.SketchfabOAuth2',
#     'social_core.backends.skyrock.SkyrockOAuth',
#     'social_core.backends.soundcloud.SoundcloudOAuth2',
#     'social_core.backends.spotify.SpotifyOAuth2',
#     'social_core.backends.stackoverflow.StackoverflowOAuth2',
#     'social_core.backends.steam.SteamOpenId',
#     'social_core.backends.stocktwits.StocktwitsOAuth2',
#     'social_core.backends.stripe.StripeOAuth2',
#     'social_core.backends.suse.OpenSUSEOpenId',
#     'social_core.backends.thisismyjam.ThisIsMyJamOAuth1',
#     'social_core.backends.trello.TrelloOAuth',
#     'social_core.backends.tripit.TripItOAuth',
#     'social_core.backends.tumblr.TumblrOAuth',
#     'social_core.backends.twilio.TwilioAuth',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.vk.VKOAuth2',
#     'social_core.backends.weibo.WeiboOAuth2',
#     'social_core.backends.wunderlist.WunderlistOAuth2',
#     'social_core.backends.xing.XingOAuth',
#     'social_core.backends.yahoo.YahooOAuth',
#     'social_core.backends.yahoo.YahooOpenId',
#     'social_core.backends.yammer.YammerOAuth2',
#     'social_core.backends.yandex.YandexOAuth2',
#     'social_core.backends.vimeo.VimeoOAuth1',
#     'social_core.backends.lastfm.LastFmAuth',
#     'social_core.backends.moves.MovesOAuth2',
#     'social_core.backends.vend.VendOAuth2',
#     'social_core.backends.email.EmailAuth',
#     'social_core.backends.username.UsernameAuth',
#     'social_core.backends.upwork.UpworkOAuth',
#     'social_core.backends.slack.SlackOAuth2'
# )

# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'common.pipeline.require_email',
#     'social_core.pipeline.mail.mail_validation',
#     'social_core.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.debug.debug',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
#     'social_core.pipeline.debug.debug'
# )