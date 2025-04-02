# What Is the Language Server Protocol?

![rw-book-cover](https://microsoft.github.io/language-server-protocol/img/favicon.svg)

## Metadata
- Author: [[microsoft.github.io]]
- Full Title: What Is the Language Server Protocol?
- Category: #articles
- Summary: The Language Server Protocol (LSP) standardizes communication between development tools and language servers, allowing features like autocomplete and error checking to be reused across different tools. A language server runs as a separate process and communicates with the tool using a simple protocol, ensuring efficient synchronization of document contents and operations. This makes it easier for developers to work with multiple programming languages without needing to implement features for each tool individually.
- URL: https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/

## Highlights
- The idea behind the *Language Server Protocol (LSP)* is to standardize the protocol for how tools and servers communicate
- From now on, the truth about the contents of the document is no longer on the file system but kept by the tool in memory. The contents now has to be synchronized between the tool and the language server.
- Not every language server can support all features defined by the protocol. LSP therefore provides ‘capabilities’. A capability groups a set of language features. A development tool and the language server announce their supported features using capabilities.
