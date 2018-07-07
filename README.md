# Pawn Tools for Sublime Text

Sublime Text is an extremely feature-rich and customisable plain-text editor.
It's customisability is powered by Python scripting and there are a huge amount
of extensions available. Sublime Text gives you an amazing toolset tailored to
speeding up your writing workflow whether that is code, articles or just quick
notes. (Example: I wrote this entire article in Sublime using an Evernote +
Markdown extension)

## Features

Here's a quick overview of my five favourite features.

### Multiple Cursors

Multiple selection By far my favourite feature. Place as many carets as you
want, select as much text as you want. Hold the CTRL button and tap the LMB to
place a caret. Or click-drag MMB to select a 'rectangle' of text. CTRL+D will
select the next instance of whatever text you have selected and ALT+F3 instantly
selects every instance.

![https://i.imgur.com/svE9Dsn.gif](https://i.imgur.com/svE9Dsn.gif)
![https://i.imgur.com/vLtXqhj.gif](https://i.imgur.com/vLtXqhj.gif)
![https://i.imgur.com/bPFhMwN.gif](https://i.imgur.com/bPFhMwN.gif)

### Mini Map

A zoomed out version of your code that you can use to scroll around. Very handy
for large files.

![https://i.imgur.com/cGd6pDH.gif](https://i.imgur.com/cGd6pDH.gif)

### Snippets

Snippets are templates of commonly used phrases that you can trigger by typing a
certain set of characters. For instance, I can type `ALS` and all the code for
an ALS hook will be inserted. Then I can tap TAB to cycle through each editable
part of the template (prefix, function name and parameters)

![https://i.imgur.com/sxkok4K.gif](https://i.imgur.com/sxkok4K.gif)

### Conversions

Convert to tabs, tab size, encoding and syntax buttons Okay, not exactly unique
to Sublime but all handily placed at the bottom right. I code with tabs, but a
lot of the time I need to push somewhere that only accepts spaces so conversion
is useful.

![https://i.imgur.com/kfZL6kf.gif](https://i.imgur.com/kfZL6kf.gif)

### Configuration

Everything is JSON, Python or XML. Settings and key bindings are all stored in
JSON format files and can be overwritten with user specific sets of settings. As
soon as a change is made, Sublime reloads the settings and updates before your
eyes! Extension scripts are written in Python and can expand the editor a lot.

## Installation

Download and install Sublime Text for your operating system on the
[official site](https://www.sublimetext.com/).

The software is available for free evaluation without any restrictions or
hindrance aside from a small message box that pops up when saving sometimes. I
encourage you support the development of this software if possible though!

## Pawn Language Plugin

I created a Pawn language pack for sublime text which includes a ton of useful
stuff such as a build configuration, syntax highlighting (modified C syntax) and
snippets for common Pawn/SA:MP boilerplate code.

### Install

You can quickly install this if you have
[Package Control](https://packagecontrol.io/) installed. Simply open the Command
Palette with CTRL+Shift+P, type `Package Control: Install Package`:

![https://i.imgur.com/TFsDiHyl.png](https://i.imgur.com/TFsDiHyl.png)

Once the list has loaded, search for the `Pawn Syntax` package and hit enter:

![https://i.imgur.com/BjiF9RIl.png](https://i.imgur.com/BjiF9RIl.png)

Now the package is installed, you need to generate a build configuration so that
Sublime Text can talk to `pawncc` - the Pawn compiler. If you came from Pawno,
the compiler is located in the Pawno directory and it's named `pawncc.exe`.

You can also install manually by getting the source from GitHub and dropping
files from the repo into the `Data\Packages\Pawn-Syntax\` directory which is
located either in your Documents, AppData or Program Files directory for Sublime
Text.

### Setup

#### For sampctl

If you use [sampctl](http://bit.ly/sampctl-thread) you don't need to do any of
this, just `sampctl package init` and select `Sublime Text` as your preferred
editor, a build configuration will be automatically generated for you.

#### For pawncc

If you came from Pawno, follow these instructions to get set up.

To set up the Pawn compiler, open
`Preferences > Package Settings > Pawn Compiler Settings > Build Settings`

Type the path to your Pawn compiler in the input panel that pops up, example:
`C:\SA-MP\Server\pawno\`

The file will be automatically named and prompt to be saved, save it in
`Data\Packages\User` (the save window may automatically open here anyway).

![https://i.imgur.com/KRAmRh2.gif](https://i.imgur.com/KRAmRh2.gif)

The file that's generated is a `.sublime-build` file and I'll go through each
line explaining what it means here.

- `cmd`: is the command to pass. You can include compiler flags such as `-d3`
  and `-Z+` in their own argument strings after this.
- `fileregex`: is a regex used to parse error/warning output. This allows you to
  double-click errors/warnings to jump directly to the file and line.
- `workingdir`: is the path to the directory where `pawncc.exe` is stored. This
  is the string that's set by your input.

### Auto-Completion

The Pawn Syntax package includes auto-complete files for all SA:MP natives as
well as a lot of popular libraries.

[Head over to this thread to read more about auto-complete and contribute.](http://forum.sa-mp.com/showthread.php?t=511195)

![https://i.imgur.com/Hd5qCuL.gif](https://i.imgur.com/Hd5qCuL.gif)

### Mapping Keys

Key bindings are stored in JSON format inside `.sublime-keymap` files. There are
default key bindings, user key bindings and package specific key binds which
conveniently overwrite each other in that reverse order.

In the Pawn Syntax package, I've included a small set of key bindings some of
which emulate Pawno and others I just find useful:

- `f3`: Find next
- `f4`: Find previous
- `ctrl+r`: Open the output panel (where warnings and errors appear)
- `f5`: Compile the current file
- `pause`: Cancels compilation (very useful if you realise you forgot something
  just after compiling!)

## Contributors

[See this page](https://github.com/Southclaws/pawn-sublime-language/graphs/contributors)
for a list of contributors to this project.
