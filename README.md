# HTML List Scraper

A script that will scrape or grab list items from a paginated webpage.

## How it works

Observe the target page for its HTML components.

Tell the script the total **items you need** and how many **items are listed per page**.

It will loop on that page count while looping for each item count.

## Example

Here we have a target page that states the page and the total items.

```html
<h2><strong>1-20</strong> of <strong>258</strong> vacancies</h2>
```

As well as the target component for each item pages. 

```html
<div class="content-article">
    <h1>Operations Engineer</h1>
    <div class="article-intro">
	    <p class="light-text"> Some-Identifier-Intro </p>
    </div>
    <div class="vacancy-content">
        This is an amazing Job, do apply.  
  </div>
</div>
```

### Observing the Target

In this example we determined that the items are inside an *< h2 >* element.

```html
<h2><strong>1-20</strong> of <strong>258</strong> vacancies</h2>
```

We now know that there are **20** items per page and there are **258** items in total. 

And we know that the URL uses the GET parameter `start` to begin each page list with a certain item and it starts at 0.

So we will use these for our variables.

```python
pages = int(h2[len(h2)-1].contents[2].text)
pages = math.ceil(pages / 20) if math.floor(pages / 20) > 0 else 1
start = 0
```

### Looping Each Page

Based on the observed HTML of the target item page:
We now know that the Title is in class `content-article.h2` and the intro is in class `article-intro` and the description is in class `vacancy-content`

```html
<div class="content-article">
    <h1>Operations Engineer</h1>
    <div class="article-intro">
	    <p class="light-text"> Some-Identifier-Intro </p>
    </div>
    <div class="vacancy-content">
        This is an amazing Job, do apply.  
  </div>
</div>
```

Now we just scrape these areas as `title`, `intro`, and `content` and set it as variables.

We now can write a CSV file based on those columns.