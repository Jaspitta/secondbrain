# Tomasulo

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/298647053/aZ5vfdnzxsXjsUKuKsLDxx4yc3x2GmVQDfa4Q3hWtRI-cove_rgwAm8V.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: Tomasulo
- Category: #articles
- Document Note: Q: Can you explain to me in simpler words the first part, the introduction of this document
   A: The introduction of this document explains a method used in a specific computer (the IBM System/360 Model 91) to make better use of its various processing units when doing arithmetic. It describes a system that allows multiple calculations to happen at the same time without needing special programming, improving overall performance. The focus is on efficiently managing how data is shared and processed between different parts of the computer.
- Summary: The paper discusses a method for improving the performance of floating-point operations in the IBM System/360 Model 91 by using multiple execution units and a Common Data Bus (CDB). This setup allows for concurrent execution of instructions, reducing delays and optimizing processing. The design includes reservation stations and a tagging system to manage data flow and maintain the correct order of operations.
- URL: https://readwise.io/reader/document_raw_content/298647053

## Highlights
- instruction unit, in preparing instructions for the floating-point operation stack (FLOS), maps both storage-to-register and register-to-register instructions into a pseudo-register-to-register forma
- R1 is always one of the four floating-point registers
- usually the sink of the instructio
- Store operations are the sole exception* wherein
  R1 specifies the 26
  source
