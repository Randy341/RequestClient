##  Request Client 
An easy-to-use library that encrypts string by applying different encryption in sequence.
Decryption is done by applying decryption with the same sequence in reverse.  

Currently supported encryptions and their dependencies:
* AES (Crypto-JS)
* DES (Crypto-JS)
* Rabbit (Crypto-JS)
* One-Time-Pad (one-time-pad-es6)

Current version supports TypeScript

## Node.js (Install)  
Requirements:
- Node.js (version 8 or above.  Need ES6 async/await and typed array)
- NPM
```bash
npm install chain-encryption
````

## Usage (Python3)
```python
    import requests
    
```

## Q&A
#### Q: Why this library needs node version 8 or above?
A: Specifically, this library requires async/await and typed array feature from ES2015.  Any node or browser version supporting
these two will suffice.  Async/await is much less important as it only served as wrapper for 
async call.  You can fork your own on github and rewrite the async/await portion.  
However, the typed array feature is a must as typed array is used heavily.  

#### Q: Your library is garbage!  I don't like it!
A: Then you open PR and improve it! Or don't use it! Nobody is begging you here...   
Look, I get it.  This library isn't super optimized.  It is optimized enough for
my project, and I published this on NPM so others may take advantage of my works.  
I know some people (like those working in G-Company) 
love writing highly optimized but long and cryptic codes without documentation.   
I prefer codes that can be easily 
and quickly understood by teammate of different experience levels so they can contribute quickly.

    
    
    

