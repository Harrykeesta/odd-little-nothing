# odd little nothing — launch decision

Use ChatGPT on iPhone for art, a pseudonymous GitHub account for publishing, and GitHub Pages for the public site. The reader is plain static HTML/CSS plus 1 KB of optional keyboard/swipe JavaScript; it has no database, tracker, visitor account, API key, or runtime server. The Sites deployment is a private review copy only: its account-derived hostname is not suitable for this anonymous launch.

## Daily workflow

Keep one ChatGPT conversation with the style instructions below and the approved `site/comics/003.webp` attached as a reference. Dictate a rough thought. Ask for a finished comic and a short transcript. Save the image. Open your bookmarked GitHub “Publish a comic” form, attach the image, paste the transcript, add a title, and submit. The included automation optimizes the image, removes EXIF, updates the archive and publishes Pages. This is deliberately a reuse of an existing form, not another admin app.

Target about two minutes of hands-on time after practice. Not a measured guarantee: image generation, free-plan limits, GitHub's queue, and publication can extend elapsed time. No live iPhone or end-to-end GitHub test has been performed. An owner issue can retry via re-running its failed workflow. Issue IDs make imports idempotent. The form and issue attachments are public: submit only final artwork and transcript, never personal notes.

## Saved art direction / prompt

You make “odd little nothing,” a deadpan three-panel microcomic. Convert my rough thought into a tiny setup, escalation, and strange final beat. Prefer understatement. No explanation after the punchline. Maximum 24 words across the strip. Choose the joke yourself; ask no questions unless essential.

Use the attached approved comic as the visual reference every time. Pip is a lumpy white pear-shaped blob with exactly three hairs, two black oval eyes, stick limbs, no clothing. Void is a floating solid black oval with two small white eyes. Wobbly heavy black marker, white ground, one acid-yellow accent (#dfff00), sparse backgrounds. No gradients, photorealism, elaborate shading, or artist imitation. Keep silhouettes, eye placement, hair count, line weight and palette unchanged. No new permanent character designs. Generate the entire three-panel strip in one image so the panels share context. Use a square canvas with three equal side-by-side panels, large readable lettering and generous margins. Return one finished image with the dialogue inside it, plus a short plain-text transcript. Keep all lettering large enough to read at 360px image width. Do not include creator names or personal identifiers.

MY THOUGHT: [dictate here]

## Consistency

Reuse the approved image itself, not just the descriptive prompt or an assumed seed. Keep one reference and the same model/workflow. Reject a draft only for a broken joke, illegible words, or a changed silhouette. Three-hair count, oval eyes, blob shape and yellow accent are the fast visual check. Reference conditioning reduces drift; it cannot guarantee exact consistency. The prototype's separate HTML captions avoid AI spelling errors, but the daily upload route accepts a finished lettered image to avoid extra editing fields.

## One-time launch setup

Create a separate pseudonymous GitHub account and public repository. Use a non-identifying account email and GitHub noreply commit email. Copy only the launch bundle into it; enable Issues and set Settings → Pages → Source to GitHub Actions. Run “Publish comic” once from Actions, then bookmark Issues → New issue → Publish a comic on your iPhone. No custom domain is required. Test one disposable comic from the actual iPhone before claiming a two-minute workflow.

Anyone can view the public code and submitted issues. Only issues created by the repository owner trigger publication; the script repeats that ownership check. No API secrets are needed. Hosting and AI providers still know the account owner: this is a public pseudonym, not anonymity from service providers.

## Research — checked 9 September 2026

- GitHub Pages is free for public repositories: https://docs.github.com/en/pages/getting-started-with-github-pages . Selected because hosting and the publishing form share one account. Static Pages limits apply: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits . Public-repository standard Actions usage is free: https://docs.github.com/en/billing/concepts/product-billing/github-actions . Use the public repo option, not private paid Pages or larger runners.
- GitHub supports issue templates and prefilled issue links: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue . This supplies the phone-friendly intake without a custom dashboard.
- Cloudflare Pages is the runner-up: free static requests and 500 builds/month, with direct upload or Git integration. It adds an account, and manual ZIP upload adds phone work. https://developers.cloudflare.com/pages/platform/limits/ and https://developers.cloudflare.com/pages/get-started/direct-upload/ . The same site folder is portable there.
- ChatGPT Free has limited image generation: https://chatgpt.com/pricing/ . Start with existing/free access; no new paid subscription is necessary to try. Availability and limits can interrupt the workflow.
- Built-in generation here consumes Codex usage: https://learn.chatgpt.com/docs/image-generation . The prototype used that existing access, without an API purchase.
- Current API alternative: GPT Image 2.5 Flare is described as OpenAI's fastest everyday image model, with $5/M text input, $8/M image input and $30/M image output tokens. https://developers.openai.com/api/docs/models/gpt-image-2.5-flare . Exact per-comic cost depends on size, quality, reference input and retries. This prototype does not call the paid API. Automated rough-thought-to-publish could use it later, but adds billing, a secret and a processing service, so it loses this launch's simplicity contest.
- Apple Shortcuts can call APIs: https://support.apple.com/guide/shortcuts/request-your-first-api-apd58d46713f/9.0/ios/26 . Not selected initially: configuring tokens, image payloads and errors is more work than a bookmarked form.

## Verification / limits

Automated checks cover every comic's navigation targets and boundaries, latest-homepage selection, local assets, owner authorization, invalid-image rejection, and duplicate publication prevention. Production output is static and works with JavaScript disabled. Image references were visually inspected. Actual mobile Safari interaction, GitHub attachment delivery, and GitHub Pages deployment need the pseudonymous account to verify. The generated framework scaffold is retained for provenance, but is not used by the static reader or the slim launch bundle; its install reported ignored optional native build scripts. The static build needs only Node and passes without them.
