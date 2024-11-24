# Block 3 Part 5 IT and the Law

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/204023330/_tl_bOrPiT-SXZ3XSCWdoAwjXDyLLm6wonJvbSFUah0-cove_ZNwyg36.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 3 Part 5 IT and the Law
- Category: #books
- Summary: The Computer Misuse Act 1990 (CMA) outlines three main offences related to unauthorized computer access. It aims to protect personal data and prosecute those who access computers without permission or intend to commit further crimes. Data protection laws, like the UK Data Protection Act, also emphasize securing personal information against unauthorized access and misuse.

## Highlights
- 2015 hack of the major UK telecom provider TalkTalk
- introduce a common hacking technique as well as two laws used to prosecute not only the hackers, but TalkTalk itself.
- we are obligated to understand the legal applications of our work
### 5.1 Anatomy of a hack
- On 21 October 2015, its website began to become unreliable before becoming completely unavailable to users
#### 5.1.1 The scale of the TalkTalk hack
- In total, 157,000 customer accounts were stolen
- complete bank or credit card records belonging to 16,000 customers, as well as partial banking details of a further 28,000 customers
- TalkTalk’s shares dropped steeply on news of the breach, and the company’s profits halved as it spent £60 million improving security
- more than 101,000 customers abandoned TalkTalk
#### 5.1.2 A long-lived hack
- The method of breaching the site’s security was identified as long ago as 1998 by the security expert Jeff Forristal
- Forristal had identified an extremely serious problem that continues to affect databases
##### SQL
- Web pages read data from, and write data to, databases using queries
- in a specialised programming language called a query language. By far the most popular query language is the Structured Query Language (SQL).
- A web browser passes data to a server by appending a query string to a web page’s URL
- a programming script extracts the contents of the query string and generates a query
##### SQL injection (SQLi)
- What became known as SQL injection (SQLi) replaces part of a legitimate SQL query with malicious instructions
- SQLi can be used to bypass authentication processes restricting access to databases
- add new records to databases, to edit data, to divulge information or even to delete data
##### Preventing SQLi‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
- SQLi attacks can be prevented with relatively little effort
- Restricting permissions
- Turning off error messages
- determined hackers often explore the computer hosting the data
- By using many such commands, an attacker can learn a great deal about a database and how it might be attacked
- Error messages are an invaluable tool when new database applications are being created; however, when the application is finished, error messages should be disabled
- Turning off error messages cannot stop SQLi; it just makes it more difficult for the attacker
- An attack where the hacker has to assume the underlying structure of the database (an assumption which may be incorrect) is known as blind injection
- it is considered good practice to sanitise query strings
- Restricting query strings
- **Parsing queries**
- a process of examining the query string for sequences of characters corresponding to SQL instructions
- parsing ensures SQL commands cannot be passed from a query string
- TalkTalk’s systems had not been hardened against SQLi.
### 5.2 The Computer Misuse Act 1990
- The requirement for national legislation outlawing computer misuse goes back to 1979
- Prestel pioneered many services we now take for granted, including up-to-the-minute news and weather information, financial results, live train times and personal advice. Prestel’s Mailbox service was the first public email service in the UK, and in 1983 Prestel introduced the world’s first online banking service through the Bank of Scotland and the Nottingham Building Society, followed by online theatre ticketing and grocery shopping.
- Prestel’s failure was largely due to the costs of using the service
#### 5.2.1 Schifreen and Gold
- In the early 1980s, the journalist Robert Schifreen saw a demonstration of Prestel at a computer exhibition. Schifreen watched as a Prestel engineer entered the userID 1234 and the password 22222222
- Prestel had enough information to accuse Schifreen and Gold of unauthorised access to their computers. In 1985 the pair were arrested for accessing the Prestel network – except…
  …there was no law forbidding unauthorised access to a computer.
##### The court cases
- The prosecution appealed the case to England’s then-highest court, the House of Lords. In 1988, the House of Lords upheld the original appeal; according to the law of 1988, Schifreen and Gold were not guilty under the Forgery and Counterfeiting Act 1981.
#### 5.2.2 The need for a computer misuse act
- the House of Lords ruling raised the prospect that Parliament would have to draft a new law
- the Computer Misuse Act 1990 (CMA) was introduced into Parliament by the backbench Conservative MP, Michael Colvin.
- A Parliamentary bill is a piece of proposed legislation usually introduced by the government
- Only after a bill has completed its passage through Parliament and been given ‘royal assent’ does it become an Act of Parliament and have legal force.
- came into effect in August 1990
#### 5.2.3 Offences under the Computer Misuse Act 1990
- Sections 1 to 3 of the CMA introduced three increasingly serious offences
- unauthorised access
- intending to commit or assist the commission of further offences
- modification of computer material.
##### Intent
- the legal concept of intent consists of two conditions:
  1. the desire to perform a crime
  2. the action of attempting to perform that crime.
- A person can only be found guilty if it can be demonstrated that both of these conditions are met.
- It is *not* illegal for me to think of a way of performing a bank robbery, or even to write it down
- The CMA cannot be used to punish accidental actions that result in people having unauthorised access
##### What is a computer?
- very wisely, the CMA does not define what is meant by a computer
- not just applicable to the types of computers used when the law came into effect
#### 5.2.4 Section 1 offences
- unauthorised access is outlined in Section 1
- intends to gain access to the computer
- are not authorised
- aware that their actions are not authorised
- punishments
- fines or imprisonment
- Summary conviction
- minor offences
- maximum punishment of one year in prison and/or a fine (usually capped at £5000)
- Conviction on indictment
- the maximum punishment is a 2-year prison sentence and/or a fine.
#### 5.2.5 Section 1 offences and argument maps
- The three supporting claims are *grouped* together. They are connected to the main claim via a single ‘SUPPORT’. In other words, the main claim only holds if supporting claim 1 *and* supporting claim 2 *and* supporting claim 3 all hold.
- Whenever supporting claims are grouped to establish the main claim, *all* supporting claims must hold
### 5.3 The Computer Misuse Act 1990 continued
#### 5.3.1 Section 2 offences
- Section 2 of the CMA are those where unauthorised access to a computer was performed with the intention of using either the computer itself, or data held on that computer, to commit further crimes
- aggravated offences.
- Section 2 is composed of five subsections
- explain how the section is to be applied
- 2(1) explains
- an offence under Section 1 *and* they intend to commit or assist crimes listed in Subsection 2(2).
- 2(2) lists types of crime covered by Section 2
- 2(3) makes it clear that the second offence
- does not need to immediately follow
- 2(4) allows for someone to be prosecuted under Section 2 even if there was no way that they could successfully have committed a further offence
- 2(5) lists the punishment
- prison sentences of up to 5 years
#### 5.3.2 Section 3 offences
- Section 3 covers offences affecting the *operation* of a computer.
- when a user intentionally modifies the contents of a computer to cause harm
- may be treated as aggravated offences since the modification of a computer can be used to commit further offences
- A bug or accidental action
- *cannot* be prosecuted under Section 3
- It is not necessary to have caused harm to having committed an offence under Section 3, so it can be used to prosecute people even if their attack was unsuccessful
- severe punishments
- summary convictions are limited to 12 months’
- juries may result in imprisonment for up to 10 years
#### 5.3.3 Amendments to the CMA
- The most important amendments are two new sections, Section 3A and Section 3ZA
##### Section 3A offences
- criminalises the action of developing or supplying software or data that is likely to be used to commit crimes
- imprisoned for up to 2 years and/or fined
- Section 3A has been strongly criticised by security professionals
- any decision to prosecute someone under Section 3A must follow careful consideration of the *likelihood* that software or data would be used to break the CMA.
- Does the software have a legitimate purpose, such as testing a network’s security?
- What was the context in which the software was used to commit the offence
##### Section 3ZA offences
- cover the most serious of all computer crimes – those affecting human lives, the environment, the economy or national security.
- extremely severe punishments
- The *least* serious Section 3ZA crimes can result in imprisonment for up to 14 years and a fine
- a life sentence and a fine
#### 5.3.4 The TalkTalk hack and the CMA
- six people had been arrested in relation to the TalkTalk hack, five of whom were charged.
### 5.4 The UK Data Protection Acts
- UK’s first data privacy law was enacted in 1981
- The issue of international safeguards on personal data has not gone away.
- The Data Protection Act 1984 introduced further data protection, requiring public and private organisations storing personal data on computers to register with a Data Protection Registrar
- Protection of personal data was made explicit in the Data Protection Act 1998
- superseded when the Data Protection Act 2018 was passed, primarily to implement the EU’s General Data Protection Regulation (GDPR).
- harmonise data protection provisions across all EU
#### 5.4.1 The GDPR and the UK
- the GDPR gives member states some flexibility
- The DPA 2018 goes beyond the GDPR
##### The purpose of GDPR
- The introduction of a single EU-wide data protection regime makes it easier for any business or organisation wishing to operate across national boundaries
- any organisation wishing to process personal data relating to EU citizens must obey GDPR even if they are based outside of the EU.
##### Enforcement
- each member country is required to have a central Supervisory Authority
- In the UK, this role is performed by an independent body, the Information Commissioner’s Office (ICO).
- requires all organisations employing more than 250 people to have at least one Data Protection Officer (DPO)
- The GDPR not only forces companies to report breaches, but they must inform the supervisory authority (SA) within 72 hours
##### Penalties
- Written warnings for relatively minor breaches
- More serious failings require organisations to undergo regular data protection audits
- The most serious incidents could result in fines of up to €20 million or 4% of an organisation’s annual global turnover
##### **Pseudonymisation**
- personal identifiers, such as a person’s name, address or social security number, are replaced with a new tag to protect that person’s privacy
- GDPR treats pseudonymous data identically to any other data
- During Parliamentary scrutiny of the Bill, the House of Lords introduced an amendment to safeguard security researchers. Section 172 of the Act allows for de-anonymisation for research purposes:
##### The right to erasure
- The intention was to enable individuals to request personal data be removed from search engine results because it was untrue or no longer relevant.
- The GDPR has adopted a more limited ‘right to erasure’, which will allow people to have personal data removed from computers either if the data was acquired by illegal methods (such as by hacking or unauthorised disclosure), or if the privacy of the person in question is seen to be more important than the interests of the organisation storing their data.
- GDPR requires data processors to process as little personal information as possible
#### 5.4.2 Enforcing UK Data Protection law
- not automatically investigated by the police, nor are the majority of breaches prosecuted in a court of law. Instead, the DPA is enforced by the Information Commissioner’s Office (ICO)
##### What is personal data?
- personal data as defined in Section 3(2) of the Act as:
  • any information relating to an identified or identifiable living individual.
##### Special categories of personal data
- special categories of personal data (‘sensitive data’):
- data create significant risks to fundamental rights and freedoms, these protections are very broadly drawn
#### 5.4.3 Data processing
- processing refers to any action involving personal data on a computer
##### Destroying data
- before deciding what measures are appropriate, you need to assess your information risk
- Many organisations require data to be securely deleted
#### 5.4.4 The GDPR and DPA 2018 principles of data protection
##### The first principle of data protection
##### Fair use of data
##### Clarity
- Consent
- There must be a clear and specific, up-front statement
- Contract
- Legal obligation
- Vital interests
- Public task
- Legitimate interests
- Principle 2
- data shall be obtained only for one or more specified, explicit and lawful purposes
- Principle 3
- not excessive in relation to the purpose
- Principle 4
- shall be accurate and, where necessary, kept up to date
- Principle 5
- shall not be kept for longer than is necessary
- Principle 6
- must be so processed in a manner that ensures appropriate security
- technical and organisational measures in place to demonstrate compliance
- 5.5 The TalkTalk hack and the DPA
- ICO performed a detailed investigation of the TalkTalk hack
- TalkTalk had inherited the hacked database during its 2009 takeover of Tiscali UK. TalkTalk had been unaware
- TalkTalk should and could have done more to safeguard its customer information. It did not and we have taken action.
- their failure to replace or patch the database
- they had not encrypted the database
- The financial costs of the hack included an estimated £15 million in lost sales caused by taking TalkTalk’s site offline and a further £40–45 million in ‘exceptional’ costs
