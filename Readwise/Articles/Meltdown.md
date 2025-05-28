# Meltdown

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/33563239/5Sg0ZlK3XzwNSfaKDin3dYl6UdZ67yX56rBuN1_tN38-cover_lqL37Jx.png)

## Metadata
- Author: [[meltdownattack.com]]
- Full Title: Meltdown
- Category: #articles
- Summary: Researchers have discovered a serious vulnerability in processors' memory isolation capabilities, called Meltdown, which allows any user process to read the entire kernel memory of the machine, including personal data and passwords. The flaw can be found on modern Intel microarchitectures since 2010 and other CPUs of other vendors potentially. The researchers recommend implementing KAISER immediately to prevent the attack.
- URL: https://meltdownattack.com/meltdown.pdf

## Highlights
- When the transient instruction sequence of step 2 is executed, exactly one cache line of the probe array is cached. The position of the cached cache line within the probe array depends only on the secret which is read in step 1. Thus, the attacker iterates over all 256 pages of the probe array and measures the access time for every ﬁrst cache line (i.e., offset) on the page. The number of the page containing the cached cache line corresponds directly to the secret value.
- With Intel TSX, multiple instructions can be grouped
  to a transaction, which appears to be an atomic operation, i.e., either all or no instruction is executed. If one instruction within the transaction fails, already executed instructions are reverted, but no exception is raised. If we wrap the code from Listing 2 with such a TSX instruction, any exception is suppressed. However, the microarchitectural effects are still visible, i.e., the cache state is persistently manipulated from within the hardware transaction [19].
