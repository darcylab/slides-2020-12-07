# slides-2020-12-07

Using [Marp](https://marp.app/)

Final slide deck as PDF: [here](https://github.com/tdemarcy/slides-2020-12-07/blob/master/slides.pdf)

```sh
# Convert slide deck into HTML
docker run -u "node" --rm -v $PWD:/home/marp/app/ -e LANG=$LANG marpteam/marp-cli slides.md --html

# Convert slide deck into PDF
docker run -u "node" --rm -v $PWD:/home/marp/app/ -e LANG=$LANG marpteam/marp-cli slides.md --allow-local-files --pdf
```

Illustrations: [2.flexiple.com/scale](https://2.flexiple.com/scale)
