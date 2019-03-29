# RevImg

## Motivation
RevImg is a lightweight package to interact with Google Reverse Image Search. I created this package as an adequate other solution did not exist. Although [MRISA](https://github.com/vivithemage/mrisa) is quite good, there are three major shortcomings:

* It only allows returns the first page of Google Reverse Image results
* It adds unnecessary overhead in that you need to run a flask server
* Individual results are not intuitively grouped (i.e. MRISA returns a list of links, a list of titles, and a list of descriptions. I think it makes more intuitive sense for each individual result to be grouped, with the result containing its link, description, and title together as one logical grouping).

This library attempts to fix these issues. For the most part, this library is very similar to MRISA: in fact, much of the BS4 code is lifted directly from it. As a minor update, I switched out the use of pycurl for requests. While this could theoretically slow down the package somewhat, in experimentation, the major bottleneck is the Google response, not the difference in library. I think that the gain in simplicity (and thus user customization) is worth the minor performance hit.

## Usage
Initialization is simple:

```
ri = RevImg()
```
You then have access to three methods. 
#### get\_best_guess()
To retrieve Google's best guess:

```
ri.get_best_guess("https://via.placeholder.com/350x150")
```
This returns a string for what Google believes the image to be.

#### get_similar()
To get a list of similar images:

```
ri.get_similar("https://via.placeholder.com/350x150")
```
This returns a list of urls, with each url being a string.

#### get\_related_results()
To get a list of sites that have images similar to the one searched for:

```
ri.get_related_results("https://via.placeholder.com/350x150")
```

This creates a generator, with each next element being a dictionary of the form: 

```
{
	"title": "title here",
	"link": "link.com",
	"description": "description..."
}
```

We utilize a generator in order to decrease the need for useless page loads (given that this is the most expensive cost). As a result, should a list be necessary, we recommend simply processing it as a list comprehension:

```
results = [ret for ret in ri.get_reelated_results("https://via.placeholder.com/350x150")
```

### Disclaimer
Please note that this library is provided AS IS. Do NOT utilize it in a way that would be against Google's ToS.

