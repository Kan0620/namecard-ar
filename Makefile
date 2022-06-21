.PHONY: deploy
deploy:
		git push heroku main

.PHONY: log
log:
		heroku logs --tail