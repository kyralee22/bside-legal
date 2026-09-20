# Privacy Policy

**Last updated: September 20, 2026**

BSIDE is an app for logging the concerts and festivals you go to. This policy explains what
information the app collects, why, who it is shared with, and how you can get rid of it.

We try to ask for as little as possible. Where we could have requested more access and chose not
to, this policy says so explicitly.

If anything here is unclear, email **bsideworkapp@gmail.com**.

---

## Information you give us

**Account information.** To create an account you provide an email address, a password, and a
username. That is the entire signup form — we do not ask for your real name, date of birth, phone
number, or gender. Passwords are handled by our authentication provider (Supabase) and are stored
as salted hashes; we never see or store your plain-text password.

**Profile information.** Optionally: a display name, a short bio, and a profile picture.

**Content you create.** The shows you log and everything attached to them — your rating, liner
notes, best song, the date and venue, any lists or superlatives you build, and the other BSIDE
users you tag as having been there with you.

**Photos.** If you add a profile picture or attach photos to a logged show, those images are
uploaded to our storage provider.

- BSIDE does **not** request access to your photo library. When you pick an image, iOS shows you
  its own picker and hands us only the specific images you chose — the app never receives, and
  cannot browse, the rest of your library.
- The app asks for camera permission only if you choose "Take Photo" for a profile picture.
- Before any image is uploaded it is re-encoded, which **strips embedded metadata** including the
  GPS coordinates, device model, and timestamp that cameras normally write into photo files.

**Search text.** When you log a show by typing a sentence like "Phoebe Bridgers at the Greek in
2022," that sentence is processed to pull out the artist, venue, city, and date. See
**AI-assisted search** below.

**Social connections.** Who you follow and who follows you.

## Information collected automatically

**Approximate location (optional).** If you grant location permission, BSIDE requests your location
at **reduced accuracy**. This is not a promise about how we handle a precise coordinate — it means
the app is built so that iOS never gives it one. The system deliberately fuzzes your position
before the app ever sees it, and iOS will show your location as approximate rather than precise.

We use it to show concerts happening near you and to identify your city. Before your coordinates
are sent onward to Ticketmaster, we round them further, to roughly a one-kilometer grid. We do not
store a history of your locations, and we do not request or use background location — the app can
only see where you are while you are using it. The app works without this permission; you simply
won't see the "near you" features.

**Basic technical data.** Our hosting provider records standard server logs (IP address, timestamp,
request path) as part of operating the service.

**What we deliberately do not collect.** BSIDE contains no analytics SDK, no advertising SDK, and
no third-party tracking or attribution libraries of any kind. We do not use the Advertising
Identifier, we do not ask for App Tracking Transparency permission, and we never request access to
your contacts, calendar, microphone, health data, or music library.

## AI-assisted search

When you log a show by typing a sentence, that sentence is sent to our server, which forwards **the
sentence text only** to OpenRouter, an AI routing service, which passes it to the underlying model
provider (currently OpenAI). The model's only job is to pull structured details — artist, venue,
city, date — out of your sentence so we can find the right show.

- Your identity is **not** sent with it. The request contains the sentence and nothing else: no
  username, no email, no account ID, no device identifier.
- We do not store the sentence in our database. The extracted details are used to search for a
  matching show and are then discarded.
- Once the sentence reaches OpenRouter and the model provider, their own retention and logging
  practices apply. See [OpenRouter's privacy policy](https://openrouter.ai/privacy).
- The feature is optional. You can skip it entirely by using the manual entry option or ordinary
  search, and nothing is sent anywhere.

Please avoid typing anything into that box you would not want processed by an outside AI service.

## Spotify (optional)

If you choose to connect Spotify, you are sent to Spotify to authorize the connection. BSIDE
requests a **single permission: read your top artists** (`user-top-read`). We do not request access
to your listening history, your saved library, your playlists, or playback control, and we cannot
post anything to your account.

The import is **one-time**. We exchange the authorization for a short-lived token, read your top
artists, and then discard the token. BSIDE stores no Spotify credentials of any kind — no password,
no access token, no refresh token — so we have no standing ability to read your Spotify account.
Refreshing your top artists requires you to authorize again.

From that import we keep **only your top artists** — artist names, Spotify artist IDs, artist
images, and genres — to display your "top rotation" on your profile and to help you find people
with similar taste. We also count top-artist data across all users in aggregate to show which
artists are popular on BSIDE; this is counted in bulk and is not presented as "this specific person
listens to X."

You can disconnect Spotify at any time from your profile, which deletes the stored artists, and
revoke BSIDE's access directly at
[spotify.com/account/apps](https://www.spotify.com/account/apps).

## What we do NOT do

- We do **not** sell your personal information.
- We do **not** share your information with advertisers, and the app contains no ads.
- We do **not** use third-party analytics, advertising, or tracking SDKs.
- We do **not** track you across other apps or websites.
- We do **not** use your content to train AI models.

## What other people can see

BSIDE is a social app, so some information is visible to others by design:

- Your username, display name, bio, profile picture, and profile statistics.
- The shows you log, your ratings, your written notes, your lists, and your superlatives.
- Who you follow and who follows you.
- If you tag another user as having attended a show with you, that user and people viewing that
  log can see the tag.

**Please treat everything you post as public.** BSIDE does not currently offer a private-profile
mode; if we add one, we will update this policy.

**Images are publicly accessible.** Profile pictures and concert photos are stored in public
storage buckets, which means anyone with the direct image URL can open it. Do not upload images you
would not be comfortable being publicly accessible.

## Who we share information with

We use a small number of service providers to run the app. They process data on our behalf:

| Provider | What they receive | Why |
|---|---|---|
| **Supabase** | Account credentials, profile, logs, photos | Hosting, authentication, database, file storage |
| **OpenRouter** (and the model provider it routes to, currently **OpenAI**) | The text of a search sentence, with no identifying information | Extracting artist / venue / date from what you typed |
| **Spotify** | A one-time authorization request | Only if you connect Spotify |
| **Ticketmaster** | Coordinates rounded to roughly a one-kilometer grid | To return concerts near you |
| **Apple** | Purchase and download data | App Store distribution |

Our catalogue of artists, venues, and past shows is compiled in advance from public music
databases such as Setlist.fm and MusicBrainz. That happens on our own servers, before you ever
search — your searches are not sent to those services.

We may also disclose information if required by law, or to protect the rights, safety, or property
of BSIDE or its users.

## Data retention and deletion

We keep your information for as long as your account exists.

You can delete your account at any time from **Profile → Settings → Delete Account**. Deleting your
account removes your profile, your logs, your lists, your Spotify top artists, and your uploaded
images. Some content may remain briefly in backups before being overwritten. Aggregated statistics
that cannot identify you may be retained.

## Security

Data is transmitted over encrypted connections (HTTPS/TLS). Your login tokens are stored in the iOS
Keychain rather than ordinary app storage. Data is stored with our hosting provider using access
rules that restrict rows to their owner, and third-party API keys are held server-side rather than
inside the app. No system is perfectly secure, and we cannot guarantee absolute security, but we
work to protect your information using industry-standard measures.

## Children

BSIDE is not directed at children under 13, and we do not knowingly collect personal information
from children under 13. If you believe a child has provided us with personal information, contact
us and we will delete it.

## Your rights

Depending on where you live, you may have the right to access, correct, export, or delete your
personal information, and to object to or restrict certain processing. Most of this is available
directly in the app — you can edit your profile, edit or delete individual logs, disconnect
Spotify, and delete your account. For anything else, email us at **bsideworkapp@gmail.com** and we
will respond within 30 days.

If you are in the EEA or UK, our legal bases for processing are: performing our contract with you
(operating your account), your consent (location, Spotify, camera), and our legitimate interests
(keeping the service secure and functional).

California residents: we do not sell or share personal information as those terms are defined by
the CCPA/CPRA.

## International users

BSIDE is operated from the United States and our service providers store data in the United States.
If you use the app from elsewhere, your information will be transferred to and processed in the
United States.

## Changes to this policy

If we make material changes to this policy, we will update the date at the top and, where
appropriate, notify you in the app. Continued use of BSIDE after a change means you accept the
updated policy.

## Contact

Questions, requests, or complaints: **bsideworkapp@gmail.com**
