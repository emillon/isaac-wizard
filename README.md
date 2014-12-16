R U a Wizard? - The Binding of Isaac : Rebirth : Augmented
----------------------------------------------------------

The Binding of Isaac: Rebirth ("TBoI:R") is a great game, but there are a lot of
items to know. The usual solution to this problem is to have the wiki always
open, but this ruins the experience a bit. Instead, this projects aims at
creating an "augmented" experience on top of the game.

Put simply, it creates an overlay above the game to identify objects and their
effects. Computer Vision is hard and I am by no means an expert, so this does
not work well.

![Example](https://i.imgur.com/4m9LDsu.png)

See! It's not even a purple heart. But it's indeed Mom's Lipstick.

How to use
----------

You need to rip sprites from the game. Assets are somehow obfuscated so it is
not so easy. I got mine from [this reddit
thread](https://www.reddit.com/r/bindingofisaac/comments/2mbz6p/wiki_folks_the_sprites_were_ripped_out_of_the_a/).

Then, it is necessary to find only object sprites. A good approximation is to
keep only 32x32 images. This will move pictures to a folder with their
resolution.

``` bash
for i in *.png ; do
    dir=$(identify -- "$i" | awk '{ print $3; }')
    [ -d "$dir" ] || mkdir "$dir"
    echo "$i -> $dir"
    mv -- "$i" "$dir"
done
```

After that, remove sprites that do not work.

Now it works:

``` bash
python multimatch.py screenshot.png sprites/32x32/
```

It will display the result. If you want to save it, add "out.png" as an extra
argument.

Stuff to do
-----------

  - live capture instead of screenshots.
  - draw on an overlay instead of generating a pic.
  - improve performance. On my old tank it takes 3s per frame.
  - assist stuff (open wiki, etc).
