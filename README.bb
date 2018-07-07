[COLOR="#FF4700"][SIZE="7"][B]Pawn Tools for Sublime Text[/B][/SIZE][/COLOR]

Sublime Text is an extremely feature-rich and customisable plain-text editor. It’s customisability is powered by Python scripting and there are a huge amount of extensions available. Sublime Text gives you an amazing toolset tailored to speeding up your writing workflow whether that is code, articles or just quick notes. (Example: I wrote this entire article in Sublime using an Evernote + Markdown extension)

[COLOR="RoyalBlue"][SIZE="6"][B]Features[/B][/SIZE][/COLOR]

Here’s a quick overview of my five favourite features.

[COLOR="DeepSkyBlue"][SIZE="5"][B]Multiple Cursors[/B][/SIZE][/COLOR]

Multiple selection By far my favourite feature. Place as many carets as you want, select as much text as you want. Hold the CTRL button and tap the LMB to place a caret. Or click-drag MMB to select a ‘rectangle’ of text. CTRL+D will select the next instance of whatever text you have selected and ALT+F3 instantly selects every instance.

[IMG]https://i.imgur.com/svE9Dsn.gif[/IMG] [IMG]https://i.imgur.com/vLtXqhj.gif[/IMG] [IMG]https://i.imgur.com/bPFhMwN.gif[/IMG]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Mini Map[/B][/SIZE][/COLOR]

A zoomed out version of your code that you can use to scroll around. Very handy for large files.

[IMG]https://i.imgur.com/cGd6pDH.gif[/IMG]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Snippets[/B][/SIZE][/COLOR]

Snippets are templates of commonly used phrases that you can trigger by typing a certain set of characters. For instance, I can type [FONT="courier new"]ALS[/FONT] and all the code for an ALS hook will be inserted. Then I can tap TAB to cycle through each editable part of the template (prefix, function name and parameters)

[IMG]https://i.imgur.com/sxkok4K.gif[/IMG]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Conversions[/B][/SIZE][/COLOR]

Convert to tabs, tab size, encoding and syntax buttons Okay, not exactly unique to Sublime but all handily placed at the bottom right. I code with tabs, but a lot of the time I need to push somewhere that only accepts spaces so conversion is useful.

[IMG]https://i.imgur.com/kfZL6kf.gif[/IMG]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Configuration[/B][/SIZE][/COLOR]

Everything is JSON, Python or XML. Settings and key bindings are all stored in JSON format files and can be overwritten with user specific sets of settings. As soon as a change is made, Sublime reloads the settings and updates before your eyes! Extension scripts are written in Python and can expand the editor a lot.

[COLOR="RoyalBlue"][SIZE="6"][B]Installation[/B][/SIZE][/COLOR]

Download and install Sublime Text for your operating system on the [URL="https://www.sublimetext.com/"]official site[/URL].

The software is available for free evaluation without any restrictions or hindrance aside from a small message box that pops up when saving sometimes. I encourage you support the development of this software if possible though!

[COLOR="RoyalBlue"][SIZE="6"][B]Pawn Language Plugin[/B][/SIZE][/COLOR]

I created a Pawn language pack for sublime text which includes a ton of useful stuff such as a build configuration, syntax highlighting (modified C syntax) and snippets for common Pawn/SA:MP boilerplate code.

[COLOR="DeepSkyBlue"][SIZE="5"][B]Install[/B][/SIZE][/COLOR]

You can quickly install this if you have [URL="https://packagecontrol.io/"]Package Control[/URL] installed. Simply open the Command Palette with CTRL+Shift+P, type [FONT="courier new"]Package Control: Install Package[/FONT]:

[IMG]https://i.imgur.com/TFsDiHyl.png[/IMG]

Once the list has loaded, search for the [FONT="courier new"]Pawn Syntax[/FONT] package and hit enter:

[IMG]https://i.imgur.com/BjiF9RIl.png[/IMG]

Now the package is installed, you need to generate a build configuration so that Sublime Text can talk to [FONT="courier new"]pawncc[/FONT] - the Pawn compiler. If you came from Pawno, the compiler is located in the Pawno directory and it’s named [FONT="courier new"]pawncc.exe[/FONT].

You can also install manually by getting the source from GitHub and dropping files from the repo into the [FONT="courier new"]Data\Packages\Pawn-Syntax\[/FONT] directory which is located either in your Documents, AppData or Program Files directory for Sublime Text.

[COLOR="DeepSkyBlue"][SIZE="5"][B]Setup[/B][/SIZE][/COLOR]

[COLOR="SlateGray"][SIZE="4"]For sampctl[/SIZE][/COLOR]

If you use [URL="http://bit.ly/sampctl-thread"]sampctl[/URL] you don’t need to do any of this, just [FONT="courier new"]sampctl package init[/FONT] and select [FONT="courier new"]Sublime Text[/FONT] as your preferred editor, a build configuration will be automatically generated for you.

[COLOR="SlateGray"][SIZE="4"]For pawncc[/SIZE][/COLOR]

If you came from Pawno, follow these instructions to get set up.

To set up the Pawn compiler, open [FONT="courier new"]Preferences > Package Settings > Pawn Compiler Settings > Build Settings[/FONT]

Type the path to your Pawn compiler in the input panel that pops up, example: [FONT="courier new"]C:\SA-MP\Server\pawno\[/FONT]

The file will be automatically named and prompt to be saved, save it in [FONT="courier new"]Data\Packages\User[/FONT] (the save window may automatically open here anyway).

[IMG]https://i.imgur.com/KRAmRh2.gif[/IMG]

The file that’s generated is a [FONT="courier new"].sublime-build[/FONT] file and I’ll go through each line explaining what it means here.

[LIST]
[*][FONT="courier new"]cmd[/FONT]: is the command to pass. You can include compiler flags such as [FONT="courier new"]-d3[/FONT]
and [FONT="courier new"]-Z+[/FONT] in their own argument strings after this.
[*][FONT="courier new"]fileregex[/FONT]: is a regex used to parse error/warning output. This allows you to
double-click errors/warnings to jump directly to the file and line.
[*][FONT="courier new"]workingdir[/FONT]: is the path to the directory where [FONT="courier new"]pawncc.exe[/FONT] is stored. This
is the string that’s set by your input.
[/LIST]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Auto-Completion[/B][/SIZE][/COLOR]

The Pawn Syntax package includes auto-complete files for all SA:MP natives as well as a lot of popular libraries.

[URL="http://forum.sa-mp.com/showthread.php?t=511195"]Head over to this thread to read more about auto-complete and contribute.[/URL]

[IMG]https://i.imgur.com/Hd5qCuL.gif[/IMG]

[COLOR="DeepSkyBlue"][SIZE="5"][B]Mapping Keys[/B][/SIZE][/COLOR]

Key bindings are stored in JSON format inside [FONT="courier new"].sublime-keymap[/FONT] files. There are default key bindings, user key bindings and package specific key binds which conveniently overwrite each other in that reverse order.

In the Pawn Syntax package, I’ve included a small set of key bindings some of which emulate Pawno and others I just find useful:

[LIST]
[*][FONT="courier new"]f3[/FONT]: Find next
[*][FONT="courier new"]f4[/FONT]: Find previous
[*][FONT="courier new"]ctrl+r[/FONT]: Open the output panel (where warnings and errors appear)
[*][FONT="courier new"]f5[/FONT]: Compile the current file
[*][FONT="courier new"]pause[/FONT]: Cancels compilation (very useful if you realise you forgot something
just after compiling!)
[/LIST]

[COLOR="RoyalBlue"][SIZE="6"][B]Contributors[/B][/SIZE][/COLOR]

[URL="https://github.com/Southclaws/pawn-sublime-language/graphs/contributors"]See this page[/URL] for a list of contributors to this project.

