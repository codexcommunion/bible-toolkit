# Enabling Structured and Interoperable Access to the Sacred Scriptures

## Abstract


## Introduction
### The Need for Structured Access to the Bible
- The Bible is one of the most widely distributed and studied texts in human history.
- Many applications (theological studies, digital libraries, AI-driven analysis, sermon preparation, etc.) require structured access to scripture.
- Existing digital Bible formats vary significantly, making interoperability a challenge.
- Existing digital Bible formats are difficult to trust, lack transparency into origins and source materials, or authoritative lineage details to discern what use cases they might serve for users.
- A standardized programming interface (API) and data format can enable consistent, efficient access across multiple platforms and use cases in a reliable, trustworthy, and transparent manner.

## Data Considerations in Scope

"The Bible" is a collection of texts--the Sacred Scriptres, with each having a complex and deep history. In order to make it accessible as structured data, we must consider these nuances with care to ensure universal accomodation in respect for the historical depth and richness.

### Identifying the Relevant Domains for Standardized Scripture Access
To design a standardized way for computer systems to interact with scripture, we need to recognize the different domains that influence how biblical texts are structured, accessed, and validated. Each domain has its own set of considerations and status values that need to be accounted for in our system.

1.  **Ecclesiastical Domains** – Religious institutions oversee and regulate certain translations and commentaries of scripture. These approvals impact whether a text is recognized for doctrinal teaching, official worship, or theological study, etc.
1. **Legal Domains** – Bible translations exist under various intellectual property protections. The legal status of a text determines how it can be accessed, distributed, and reproduced.
2. **Canonical Domains** – Different religious traditions recognize different collections of texts as scripture. This domain categorizes books based on their acceptance within various canons.
3. **Linguistic Domains** – The Bible exists in thousands of languages, and translations range from highly literal to paraphrased versions.
4. **Textual Domains** – The Bible has been preserved in multiple manuscript traditions, some of which contain textual variations. Understanding these traditions is crucial for biblical scholars and textual critics.


#### Domain Discussion and Exploration
The above domains form the foundation for structuring a standardized approach to scripture access. By recognizing these influences, a digital scripture interface can ensure that users retrieve the most appropriate text based on their theological, legal, and scholarly requirements and use cases.

---

##### Ecclesiastical Domain Discussion
The Ecclesiastical Domain governs the approval and recognition of biblical texts by religious authorities. Different Christian and Jewish traditions have their own institutions responsible for evaluating texts and so we must consider the best way to capture the status of the evaluation process.

###### Ecclesiastical Governing Bodies Considered

Different governing bodies may exist for various traditions, and each may have their own internal hierarchical structure that we need to consider and take into account. As an initial criteria, membership rates would indicate the degree of reach and impact of this project on other humans, and so should be a top consideration. Another consideration, from a practical aspect, would be the degree of open-ness and internal structure and standardization for the various bodies (is is practical to identify evaluation status from each body).

###### Catholic Church

| Governing Body                         | Approximate Membership | Data Source | Retrieval Date |
|----------------------------------------|------------------------|-------------|----------------|
| **Latin Church**                       | 1.311 billion          | [Wikipedia](https://en.wikipedia.org/wiki/Catholic_Church) | 2025-03-18 |
| **Eastern Catholic Churches**          | 18 million             | [Wikipedia](https://en.wikipedia.org/wiki/Eastern_Catholic_Churches) | 2025-03-18 |
| *Total*                                | *1.329 billion*        |             |                |

###### Eastern Orthodox Church

| Governing Body                         | Approximate Membership | Data Source | Retrieval Date |
|----------------------------------------|------------------------|-------------|----------------|
| **Ecumenical Patriarchate of Constantinople** | Varies by region       | [Wikipedia](https://en.wikipedia.org/wiki/Eastern_Orthodox_Church) | 2025-03-18 |
| **Greek Orthodox Church of Alexandria**       | Varies by region       | [Wikipedia](https://en.wikipedia.org/wiki/Greek_Orthodox_Church_of_Alexandria) | 2025-03-18 |
| **Greek Orthodox Church of Antioch**          | Varies by region       | [Wikipedia](https://en.wikipedia.org/wiki/Greek_Orthodox_Church_of_Antioch) | 2025-03-18 |
| **Russian Orthodox Church (Moscow Patriarchate)** | 150 million            | [Wikipedia](https://en.wikipedia.org/wiki/Russian_Orthodox_Church) | 2025-03-18 |
| **Serbian Orthodox Church**                   | 8 million              | [Wikipedia](https://en.wikipedia.org/wiki/Serbian_Orthodox_Church) | 2025-03-18 |
| **Romanian Orthodox Church**                  | 19 million             | [Wikipedia](https://en.wikipedia.org/wiki/Romanian_Orthodox_Church) | 2025-03-18 |
| **Bulgarian Orthodox Church**                 | 6 million              | [Wikipedia](https://en.wikipedia.org/wiki/Bulgarian_Orthodox_Church) | 2025-03-18 |
| **Georgian Orthodox Church**                  | 3.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/Georgian_Orthodox_Church) | 2025-03-18 |
| **Church of Cyprus**                          | 0.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/Church_of_Cyprus) | 2025-03-18 |
| **Greek Orthodox Church of Jerusalem**        | Varies by region       | [Wikipedia](https://en.wikipedia.org/wiki/Greek_Orthodox_Church_of_Jerusalem) | 2025-03-18 |
| **Orthodox Church in America**                | 0.1 million            | [Wikipedia](https://en.wikipedia.org/wiki/Orthodox_Church_in_America) | 2025-03-18 |
| *Total*                                       | *Approximately 220 million* |             |                |

###### Oriental Orthodox Churches

| Governing Body                         | Approximate Membership | Data Source | Retrieval Date |
|----------------------------------------|------------------------|-------------|----------------|
| **Coptic Orthodox Church of Alexandria**     | 10 million             | [Wikipedia](https://en.wikipedia.org/wiki/Coptic_Orthodox_Church_of_Alexandria) | 2025-03-18 |
| **Ethiopian Orthodox Tewahedo Church**       | 36 million             | [Wikipedia](https://en.wikipedia.org/wiki/Ethiopian_Orthodox_Tewahedo_Church) | 2025-03-18 |
| **Eritrean Orthodox Tewahedo Church**        | 2 million              | [Wikipedia](https://en.wikipedia.org/wiki/Eritrean_Orthodox_Tewahedo_Church) | 2025-03-18 |
| **Armenian Apostolic Church**                | 9 million              | [Wikipedia](https://en.wikipedia.org/wiki/Armenian_Apostolic_Church) | 2025-03-18 |
| **Syriac Orthodox Church**                   | 5 million              | [Wikipedia](https://en.wikipedia.org/wiki/Syriac_Orthodox_Church) | 2025-03-18 |
| **Malankara Orthodox Syrian Church**         | 2.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/Malankara_Orthodox_Syrian_Church) | 2025-03-18 |
| *Total*                                      | *Approximately 64.5 million* |             |                |

###### Anglican Communion

| Governing Body                         | Approximate Membership | Data Source | Retrieval Date |
|----------------------------------------|------------------------|-------------|----------------|
| **Church of Nigeria**                        | 18 million             | [Wikipedia](https://en.wikipedia.org/wiki/Church_of_Nigeria) | 2025-03-18 |
| **Church of England**                        | 26 million             | [Wikipedia](https://en.wikipedia.org/wiki/Church_of_England) | 2025-03-18 |
| **Church of Uganda**                         | 8 million              | [Wikipedia](https://en.wikipedia.org/wiki/Church_of_Uganda) | 2025-03-18 |
| **Anglican Church of Australia**             | 3.1 million            | [Wikipedia](https://en.wikipedia.org/wiki/Anglican_Church_of_Australia) | 2025-03-18 |
| **Episcopal Church (USA)**                   | 1.6 million            | [Wikipedia](https://en.wikipedia.org/wiki/Episcopal_Church_(United_States)) | 2025-03-18 |
| **Anglican Church of Canada**                | 0.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/Anglican_Church_of_Canada) | 2025-03-18 |
| *Total*                                      | *Approximately 85 million worldwide* |             |                |

###### Protestant Denominations

| Denomination                             | Approximate Membership | Data Source | Retrieval Date |
|------------------------------------------|------------------------|-------------|----------------|
| **Southern Baptist Convention**          | 13.2 million           | [Wikipedia](https://en.wikipedia.org/wiki/Southern_Baptist_Convention) | 2025-03-18 |
| **United Methodist Church**              | 5.4 million            | [Wikipedia](https://en.wikipedia.org/wiki/United_Methodist_Church) | 2025-03-18 |
| **Evangelical Lutheran Church in America (ELCA)** | 2.8 million | [Wikipedia](https://en.wikipedia.org/wiki/Evangelical_Lutheran_Church_in_America) | 2025-03-18 |
| **Assemblies of God**                    | 2.9 million            | [Wikipedia](https://en.wikipedia.org/wiki/Assemblies_of_God) | 2025-03-18 |
| **Presbyterian Church (USA)**            | 1.1 million            | [Wikipedia](https://en.wikipedia.org/wiki/Presbyterian_Church_(USA)) | 2025-03-18 |
| **Church of God in Christ**              | 5.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/Church_of_God_in_Christ) | 2025-03-18 |
| **African Methodist Episcopal Church**   | 2.5 million            | [Wikipedia](https://en.wikipedia.org/wiki/African_Methodist_Episcopal_Church) | 2025-03-18 |
| **Episcopal Church**                     | 1.4 million            | [Wikipedia](https://en.wikipedia.org/wiki/Episcopal_Church_(United_States)) | 2025-03-18 |
| *Total*                                  | *Varies significantly worldwide* |             |                |

As the various Governing Bodies may operate in geographical regions with different languages, they may also have internal sub-bodies responsible for specific translations into any given language. As such, the final evaluation and verdicts may be more complex or difficult to identify for Governing Bodies which have insufficient internal authority structure and mechanisms for expressing such evaluation verdicts.

###### Translation and Evaluation Authorities within Governing Bodies

**Catholic Church (Latin & Eastern Rites)**

| Sub-Body | Regional Language | Final Authority for Approval |
|----------|------------------|-----------------------------|
| **United States Conference of Catholic Bishops (USCCB)** | English (USA) | Dicastery for the Doctrine of the Faith (DDF) |
| **Catholic Bishops' Conference of England & Wales** | English (UK) | Dicastery for the Doctrine of the Faith (DDF) |
| **Canadian Conference of Catholic Bishops (CCCB)** | English, French | Dicastery for the Doctrine of the Faith (DDF) |
| **Conferencia Episcopal Española** | Spanish (Spain) | Dicastery for the Doctrine of the Faith (DDF) |
| **Conferencia del Episcopado Mexicano (CEM)** | Spanish (Mexico, Latin America) | Dicastery for the Doctrine of the Faith (DDF) |
| **Federación Bíblica Católica (FEBIC) - Catholic Biblical Federation** | Global Catholic translations | Dicastery for the Doctrine of the Faith (DDF) |

---
**Eastern Orthodox Church**

| Sub-Body | Regional Language | Final Authority for Approval |
|----------|------------------|-----------------------------|
| **Russian Orthodox Synodal Bible Commission** | Russian | Holy Synod of the Russian Orthodox Church |
| **Hellenic Bible Society** | Greek | Ecumenical Patriarchate of Constantinople |
| **Serbian Orthodox Biblical Commission** | Serbian | Holy Synod of the Serbian Orthodox Church |
| **Romanian Patriarchate Translation Office** | Romanian | Holy Synod of the Romanian Orthodox Church |
| **Arabic Biblical Committees (Antiochian Orthodox Church)** | Arabic | Holy Synod of the Antiochian Orthodox Church |
| **Orthodox Church in America (OCA) Liturgical Commission** | English | Holy Synod of the Orthodox Church in America |

---
 **Oriental Orthodox Church**

| Sub-Body | Regional Language | Final Authority for Approval |
|----------|------------------|-----------------------------|
| **Coptic Orthodox Holy Synod** | Coptic, Arabic | Pope of the Coptic Orthodox Church |
| **Ethiopian Orthodox Patriarchate** | Ge'ez, Amharic | Patriarch of the Ethiopian Orthodox Church |
| **Armenian Catholicosate Translation Office** | Armenian | Catholicos of All Armenians |
| **Syriac Orthodox Synodal Translation Office** | Syriac | Patriarch of the Syriac Orthodox Church |

---
**Anglican Communion**

| Sub-Body | Regional Language | Final Authority for Approval |
|----------|------------------|-----------------------------|
| **Church of England Liturgical Commission** | English (UK) | Archbishop of Canterbury |
| **Anglican Council of Canada** | English, French | Anglican Primate of Canada |
| **Episcopal Church (USA) Standing Commission on Liturgy** | English (USA) | Presiding Bishop of The Episcopal Church |
| **Church of Nigeria (Anglican) Translation Team** | Yoruba, Igbo | Archbishop of Nigeria |

---
**Protestant Denominations**

| Sub-Body | Regional Language | Final Authority for Approval |
|----------|------------------|-----------------------------|
| **Holman Bible Publishers (Southern Baptist Convention)** | English | Independent, no central authority |
| **American Bible Society (United Methodist Church)** | English | United Methodist Publishing House |
| **Lutheran Bible Translation Committee (ELCA)** | English, German | Evangelical Lutheran Church in America Synod |
| **FireBible Editorial Team (Assemblies of God)** | English | Assemblies of God Leadership Council |
| **Presbyterian Bible Translation Board** | English | Presbyterian Church (USA) General Assembly |


###### Governing Body Evaluations and Verdicts

The first aspect is the status of the evaluation itself, and the second aspect is the result of the evaluation. While different governing bodies may have different statuses and evaluation processes, this high level abstraction should accommodate all.

Each Governing Body (e.g., Catholic Church, Orthodox Synods, Protestant Denominations, Jewish Authorities) should thus be capable of identifying:

- **Evaluation Status** – Tracks where the text is in the review process.

- **Evaluation Verdict** – The final decision made after the evaluation.

###### Evaluation Status Reference Table

| Evaluation Status            | Description                                                 | Examples |
|------------------------------|-------------------------------------------------------------|----------|
| **Not Known to have been Submitted for Review** | The text has not been formally submitted for evaluation.    | AI-generated translations, personal translations. |
| **Pending Submission**       | The text is being prepared for review but not submitted yet. | A new translation awaiting church approval. |
| **Under Review**             | The governing body is actively evaluating the text.         | A Catholic translation being reviewed by a Bishop. |
| **Review Suspended**         | The review process has been paused or delayed indefinitely. | A disputed text requiring further discussion. |
| **Review Completed**         | The governing body has reached a decision and issued a verdict. | The New American Bible (NAB) after Catholic approval. |

###### Evaluation Verdict 
After an evalation has been performed, the verdict can fall into multiple broad categories such as various forms of Approval, Neutral, or Rejection/Condemnation.

###### Approval Verdicts
| Verdict                     | Description                                                | Examples |
|-----------------------------|------------------------------------------------------------|----------|
| **Imprimatur Granted**       | Approved by a Catholic bishop for publication.            | Douay-Rheims, Nova Vulgata. |
| **Nihil Obstat**            | Certified free from doctrinal errors by a Catholic reviewer. | Catholic study Bibles. |
| **Liturgical Use Approved**  | Authorized for use in official worship services.          | Septuagint Psalms (Orthodox), NAB (Catholic). |
| **Papal Recognition**        | Explicitly endorsed by the Pope or Vatican decree.        | Nova Vulgata. |
| **Synodal Approval**         | Recognized by an Orthodox Church Synod.                   | Russian Synodal Bible. |
| **Patriarchal Recognition**  | Endorsed by a Patriarch (Greek, Russian, Coptic, etc.).   | Slavonic Bible. |
| **Denominational Endorsement** | Officially recognized by a Protestant denomination.     | NIV (Evangelical), ESV (Reformed). |
| **Translation Committee Approved** | Approved by a scholarly translation committee.     | CSB (Southern Baptist), NASB (Evangelical Scholars). |
| **Rabbinic Endorsement**     | Approved by rabbinic authorities as a faithful Jewish translation. | Masoretic Text, JPS Tanakh. |
| **Recommended for Study**    | Not officially used in worship but encouraged for academic study. | RSV-CE (Catholic), Brenton’s LXX. |

###### Non-Approval / Neutral Verdicts
| Verdict                         | Description                                       | Examples |
|---------------------------------|---------------------------------------------------|----------|
| **Not Approved**                | Reviewed but lacks official recognition.         | KJV (widely used but not formally approved). |
| **Apocryphal but Not Heretical** | Not canonical but tolerated for study.           | Gospel of Thomas. |
| **Theologically Questionable**   | Contains deviations from standard doctrine.      | Masoretic Text (Orthodox perspective). |

###### Rejected / Condemned Verdicts
| Verdict                  | Description                                           | Examples |
|--------------------------|-------------------------------------------------------|----------|
| **Doctrinally Inaccurate** | Contains theological errors or distortions.        | New World Translation (Jehovah’s Witnesses). |
| **Rejected as Canonical** | Explicitly excluded from the scriptural canon.      | Gospel of Mary, Shepherd of Hermas. |
| **Condemned as Heretical** | Declared dangerous to faith by the church.        | Gospel of Judas, Marcionite Gospel. |
| **Prohibited (Historical)** | Previously listed on the Index of Forbidden Books. | Certain Gnostic texts. |

###### Data Structure Discussion

The nature of the data being represented and how varied the Governing Bodies can be requires an identification approach that can accomodate these structures.

For example, a common practice is to use a "namespace" in software to logically group items hierarchically, and a similar approach can be used to form unique identifiers for each governing body while also expressing the hierarchical nature where they fit.

**Generalized Form**

```
CHRISTIAN::<TRADITION>::<CHURCH_ORGANIZATION>::<OPTIONAL_SUBLEVEL>...
```

**Reference Table for Common Governing Bodies in Consideration**


| ID                                                                          | Name                                                            | Description                                                                                                                   |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **CHRISTIAN::CATHOLIC::VATICAN**                                            | Vatican (Holy See)                                              | The supreme governance of the Catholic Church, under the Pope.                                                               |
| **CHRISTIAN::CATHOLIC::VATICAN::DDF**                                       | Dicastery for the Doctrine of the Faith (DDF)                   | A primary dicastery under the Vatican, responsible for safeguarding doctrine.                                                |
| **CHRISTIAN::CATHOLIC::VATICAN::USCCB**                                     | United States Conference of Catholic Bishops (USCCB)            | National bishops’ conference for the USA; approvals apply regionally.                                                        |
| **CHRISTIAN::CATHOLIC::VATICAN::ENGLAND_WALES**                             | Catholic Bishops' Conference of England & Wales                 | Oversees Catholic translations in England & Wales.                                                                           |
| **CHRISTIAN::CATHOLIC::VATICAN::CCCB**                                      | Canadian Conference of Catholic Bishops (CCCB)                  | National bishops’ conference for Canada.                                                                                    |
| **CHRISTIAN::CATHOLIC::VATICAN::ESPANOLA**                                  | Conferencia Episcopal Española                                  | Responsible for Spanish-language approvals in Spain.                                                                         |
| **CHRISTIAN::CATHOLIC::VATICAN::MEXICAN_EPISCOPADO**                        | Conferencia del Episcopado Mexicano (CEM)                       | Spanish-language approvals for Mexico and parts of Latin America.                                                            |
| **CHRISTIAN::CATHOLIC::VATICAN::FEBIC**                                     | Federación Bíblica Católica (FEBIC)                             | Coordinates global Catholic biblical apostolates.                                                                            |
| **CHRISTIAN::EASTERN_ORTHODOX::MOSCOW_PATRIARCHATE**                       | Moscow Patriarchate (Russian Orthodox Church)                   | Largest autocephalous Eastern Orthodox Church, headquartered in Moscow.                                                     |
| **CHRISTIAN::EASTERN_ORTHODOX::MOSCOW_PATRIARCHATE::SYNODAL_BIBLE_COMMISSION** | Russian Orthodox Synodal Bible Commission                       | Oversees Russian Orthodox Bible translations.                                                                                |
| **CHRISTIAN::EASTERN_ORTHODOX::MOSCOW_PATRIARCHATE::HOLY_SYNOD**           | Holy Synod of the Russian Orthodox Church                       | Central governing synod for the Moscow Patriarchate.                                                                        |
| **CHRISTIAN::EASTERN_ORTHODOX::CONSTANTINOPLE**                            | Ecumenical Patriarchate of Constantinople                       | Historically the “first among equals” of the Eastern Orthodox Churches.                                                     |
| **CHRISTIAN::EASTERN_ORTHODOX::CONSTANTINOPLE::HELLENIC_BIBLE_SOCIETY**    | Hellenic Bible Society                                          | Oversees Greek translations under Constantinople’s auspices.                                                                |
| **CHRISTIAN::EASTERN_ORTHODOX::CONSTANTINOPLE::ECUMENICAL_PATRIARCHATE**   | Ecumenical Patriarchate (Authority Seat)                        | Final authority for the Ecumenical Patriarchate.                                                                            |
| **CHRISTIAN::EASTERN_ORTHODOX::SERBIAN_PATRIARCHATE**                      | Serbian Orthodox Church (Patriarchate)                          | Autocephalous Eastern Orthodox Church in Serbia.                                                                            |
| **CHRISTIAN::EASTERN_ORTHODOX::SERBIAN_PATRIARCHATE::BIBLICAL_COMMISSION** | Serbian Orthodox Biblical Commission                            | Commission overseeing Serbian Orthodox scriptural translations.                                                             |
| **CHRISTIAN::EASTERN_ORTHODOX::SERBIAN_PATRIARCHATE::HOLY_SYNOD**          | Holy Synod of the Serbian Orthodox Church                       | Governing synod for official doctrinal/liturgical decisions in Serbia.                                                      |
| **CHRISTIAN::EASTERN_ORTHODOX::ROMANIAN_PATRIARCHATE**                     | Romanian Orthodox Church (Patriarchate)                         | Autocephalous Eastern Orthodox Church of Romania.                                                                           |
| **CHRISTIAN::EASTERN_ORTHODOX::ROMANIAN_PATRIARCHATE::TRANSLATION_OFFICE** | Romanian Patriarchate Translation Office                        | Office that handles Romanian Orthodox biblical translations.                                                                |
| **CHRISTIAN::EASTERN_ORTHODOX::ROMANIAN_PATRIARCHATE::HOLY_SYNOD**         | Holy Synod of the Romanian Orthodox Church                      | Central authority for Romanian Orthodox translations and worship.                                                           |
| **CHRISTIAN::EASTERN_ORTHODOX::ANTIOCHIAN_PATRIARCHATE**                   | Antiochian Orthodox Church (Patriarchate)                       | Historically centered in Antioch (now based in Damascus); an autocephalous Orthodox Church.                                  |
| **CHRISTIAN::EASTERN_ORTHODOX::ANTIOCHIAN_PATRIARCHATE::ARABIC_BIBLICAL_COMMITTEES** | Arabic Biblical Committees (Antiochian Orthodox Church) | Oversees Arabic translations within the Antiochian Orthodox Church.                                                         |
| **CHRISTIAN::EASTERN_ORTHODOX::ANTIOCHIAN_PATRIARCHATE::HOLY_SYNOD**       | Holy Synod of the Antiochian Orthodox Church                    | Highest authority for the Antiochian Orthodox Church.                                                                       |
| **CHRISTIAN::EASTERN_ORTHODOX::OCA**                                       | Orthodox Church in America (OCA)                                | Autocephalous Orthodox Church primarily in North America.                                                                   |
| **CHRISTIAN::EASTERN_ORTHODOX::OCA::LITURGICAL_COMMISSION**                | Orthodox Church in America Liturgical Commission                | Oversees English liturgical/scriptural texts for the OCA.                                                                   |
| **CHRISTIAN::EASTERN_ORTHODOX::OCA::HOLY_SYNOD**                           | Holy Synod of the Orthodox Church in America                    | Highest authority within the OCA.                                                                                           |
| **CHRISTIAN::ORIENTAL_ORTHODOX::COPTIC_ORTHODOX_CHURCH**                   | Coptic Orthodox Church                                          | Based in Egypt; one of the Oriental Orthodox Churches.                                                                      |
| **CHRISTIAN::ORIENTAL_ORTHODOX::COPTIC_ORTHODOX_CHURCH::HOLY_SYNOD**       | Coptic Orthodox Holy Synod                                      | Governing synod for the Coptic Orthodox Church.                                                                             |
| **CHRISTIAN::ORIENTAL_ORTHODOX::COPTIC_ORTHODOX_CHURCH::POPE**             | Pope of the Coptic Orthodox Church                              | Supreme head (Patriarch) of the Coptic Orthodox Church.                                                                     |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ETHIOPIAN_ORTHODOX_CHURCH**                | Ethiopian Orthodox Church                                       | Largest Oriental Orthodox body; based primarily in Ethiopia.                                                                |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ETHIOPIAN_ORTHODOX_CHURCH::PATRIARCHATE**  | Ethiopian Orthodox Patriarchate                                 | Manages scriptural translations in Ge'ez, Amharic, etc.                                                                     |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ETHIOPIAN_ORTHODOX_CHURCH::PATRIARCH**     | Patriarch of the Ethiopian Orthodox Church                      | Highest ecclesiastical authority for Ethiopian Orthodoxy.                                                                  |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ARMENIAN_APOSTOLIC_CHURCH**               | Armenian Apostolic Church                                       | National church of the Armenian people; one of the oldest Christian communities.                                           |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ARMENIAN_APOSTOLIC_CHURCH::CATHOLICOSATE** | Armenian Catholicosate Translation Office                       | Coordinates Armenian Orthodox scriptural translations.                                                                      |
| **CHRISTIAN::ORIENTAL_ORTHODOX::ARMENIAN_APOSTOLIC_CHURCH::CATHOLICOS_OF_ALL_ARMENIANS** | Catholicos of All Armenians                      | Supreme head of the Armenian Apostolic Church.                                                                             |
| **CHRISTIAN::ORIENTAL_ORTHODOX::SYRIAC_ORTHODOX_CHURCH**                   | Syriac Orthodox Church                                          | One of the Oriental Orthodox Churches, based in the Middle East.                                                            |
| **CHRISTIAN::ORIENTAL_ORTHODOX::SYRIAC_ORTHODOX_CHURCH::SYNODAL_TRANSLATION_OFFICE** | Syriac Orthodox Synodal Translation Office       | Oversees Syriac Orthodox biblical translations.                                                                            |
| **CHRISTIAN::ORIENTAL_ORTHODOX::SYRIAC_ORTHODOX_CHURCH::PATRIARCH**        | Patriarch of the Syriac Orthodox Church                         | Highest authority in the Syriac Orthodox Church.                                                                           |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_ENGLAND**                                 | Church of England                                               | The mother church of the Anglican Communion.                                                                               |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_ENGLAND::ARCHBISHOP_OF_CANTERBURY**       | Archbishop of Canterbury                                        | Principal leader of the Church of England; symbolic figure of the worldwide Anglican Communion.                             |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_ENGLAND::LITURGICAL_COMMISSION**          | Church of England Liturgical Commission                         | Oversees liturgical and biblical texts for the Church of England.                                                          |
| **CHRISTIAN::ANGLICAN::CANADA**                                           | Anglican Church of Canada                                       | National branch of the Anglican Communion in Canada.                                                                       |
| **CHRISTIAN::ANGLICAN::CANADA::PRIMATE**                                  | Anglican Primate of Canada                                     | Senior archbishop overseeing the Anglican Church of Canada.                                                               |
| **CHRISTIAN::ANGLICAN::CANADA::ANGLICAN_COUNCIL**                         | Anglican Council of Canada                                      | Manages Anglican translations and liturgical updates in Canada.                                                           |
| **CHRISTIAN::ANGLICAN::ECUSA**                                            | Episcopal Church (USA)                                          | The Anglican Communion’s presence in the United States.                                                                   |
| **CHRISTIAN::ANGLICAN::ECUSA::PRESIDING_BISHOP**                          | Presiding Bishop of The Episcopal Church                        | Chief pastor and primate of the Episcopal Church (USA).                                                                   |
| **CHRISTIAN::ANGLICAN::ECUSA::STANDING_COMMISSION_ON_LITURGY**            | Episcopal Church (USA) Standing Commission on Liturgy           | Responsible for biblical and liturgical texts within the Episcopal Church (USA).                                          |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_NIGERIA**                                | Church of Nigeria (Anglican)                                    | Provincial church of the Anglican Communion in Nigeria.                                                                   |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_NIGERIA::ARCHBISHOP**                    | Archbishop of Nigeria                                           | Primate of the Church of Nigeria (Anglican Communion).                                                                    |
| **CHRISTIAN::ANGLICAN::CHURCH_OF_NIGERIA::TRANSLATION_TEAM**              | Church of Nigeria (Anglican) Translation Team                   | Handles Anglican translations in local languages such as Yoruba and Igbo.                                                |
| **CHRISTIAN::PROTESTANT::SBC**                                            | Southern Baptist Convention (SBC)                                | A major Protestant denomination in the USA with congregational polity.                                                   |
| **CHRISTIAN::PROTESTANT::SBC::HOLMAN_BIBLE_PUBLISHERS**                   | Holman Bible Publishers                                         | Publishes Bible translations and materials for the SBC.                                                                   |
| **CHRISTIAN::PROTESTANT::SBC::NO_CENTRAL_AUTHORITY**                      | Independent, no central authority                               | SBC has congregational autonomy; no single top authority for approvals.                                                  |
| **CHRISTIAN::PROTESTANT::UMC**                                            | United Methodist Church (UMC)                                   | A mainline Protestant denomination with connections worldwide.                                                           |
| **CHRISTIAN::PROTESTANT::UMC::AMERICAN_BIBLE_SOCIETY**                    | American Bible Society (United Methodist Church)                | Publishes and disseminates scripture for the UMC in the USA.                                                             |
| **CHRISTIAN::PROTESTANT::UMC::PUBLISHING_HOUSE**                          | United Methodist Publishing House                               | Official UMC publications, including Bibles and other church materials.                                                  |
| **CHRISTIAN::PROTESTANT::ELCA**                                           | Evangelical Lutheran Church in America (ELCA)                   | Largest Lutheran denomination in the USA.                                                                                |
| **CHRISTIAN::PROTESTANT::ELCA::LUTHERAN_BIBLE_TRANSLATION_COMMITTEE**     | Lutheran Bible Translation Committee (ELCA)                     | Handles official translation initiatives for the ELCA.                                                                    |
| **CHRISTIAN::PROTESTANT::ELCA::SYNOD**                                    | Evangelical Lutheran Church in America Synod                    | Synod-level authority providing doctrinal and liturgical approvals.                                                      |
| **CHRISTIAN::PROTESTANT::AOG**                                            | Assemblies of God (AOG)                                         | A major Pentecostal denomination.                                                                                        |
| **CHRISTIAN::PROTESTANT::AOG::FIREBIBLE_EDITORIAL_TEAM**                  | FireBible Editorial Team (Assemblies of God)                    | Produces the FireBible editions used in Pentecostal/Assemblies of God contexts.                                          |
| **CHRISTIAN::PROTESTANT::AOG::LEADERSHIP_COUNCIL**                        | Assemblies of God Leadership Council                            | Governing body that provides guidance and approvals for AG publications.                                                |
| **CHRISTIAN::PROTESTANT::PCUSA**                                          | Presbyterian Church (USA)                                       | Mainline Protestant denomination under Reformed tradition.                                                               |
| **CHRISTIAN::PROTESTANT::PCUSA::PRESBYTERIAN_BIBLE_TRANSLATION_BOARD**    | Presbyterian Bible Translation Board                            | Oversees PC(USA) translation and revision projects.                                                                      |
| **CHRISTIAN::PROTESTANT::PCUSA::GENERAL_ASSEMBLY**                        | Presbyterian Church (USA) General Assembly                      | Highest council of the PC(USA), authority over doctrinal and translation approvals.                                     |

---

##### Ecclesiastical Domain Data Entity Structure

After considering the above details regarding governing bodies, and evaluations they may perform on scriptural texts, the following data object should be capable of accomodating the data needs under this domain.

**EcclesiasticalEvaluation Entity**

*Data Fields*

- **governingBodyId**  
  - **Type**: string  
  - **Example**: `CHRISTIAN::CATHOLIC::VATICAN::USCCB`  
  - **Description**:  
    A unique ID (namespace-style) for the ecclesiastical body issuing or conducting the evaluation.

- **evaluationStatus**  
  - **Type**: string (enum)  
  - **Common Values**:
    - `Not Known to have been Submitted for Review`
    - `Pending Submission`
    - `Under Review`
    - `Review Suspended`
    - `Review Completed`
  - **Description**:  
    Indicates the current stage of review by the governing body.

- **evaluationVerdict**  
  - **Type**: string (enum) or null  
  - **Common Values**:
    - `Nihil Obstat`
    - `Imprimatur Granted`
    - (etc.)
  - **Description**:  
    The final decision if the review is completed. If under review, can be `null` or omitted.

- **decisionDate**  
  - **Type**: string (date) or null  
  - **Example**: `2025-06-01`  
  - **Description**:  
    The date on which the final verdict was issued (standard ISO 8601 format). If no final verdict, leave as null.

- **links** (optional)  
  - **Type**: object  
  - **Description**:  
    A container for HATEOAS-style references or external resources.  
    - Keys like `officialDocument`, `reviewProgress`, etc.  
    - Each key’s value should be an object with:
      - **href**: URL to the resource (e.g., PDF, HTML).  
      - **title**: Display title for that resource.  
      - **type**: MIME type (`application/pdf`, `text/html`, etc.).

**JSON made-up example**

```json
{
  "governingBodyId": "CHRISTIAN::CATHOLIC::VATICAN::USCCB",
  "evaluationStatus": "Review Completed",
  "evaluationVerdict": "Nihil Obstat",
  "decisionDate": "2025-09-12",
  "links": {
    "officialDocument": {
      "href": "https://example.org/usccb/nihil-obstat-document-2025.pdf",
      "title": "USCCB Nihil Obstat Approval",
      "type": "application/pdf"
    },
    "additionalNotes": {
      "href": "https://example.org/usccb/notes/2025-review",
      "title": "Detailed Review Notes",
      "type": "text/html"
    }
  }
}
```

**YAML made-up example**

```yaml
governingBodyId: "CHRISTIAN::CATHOLIC::VATICAN::USCCB"
evaluationStatus: "Review Completed"
evaluationVerdict: "Nihil Obstat"
decisionDate: "2025-09-12"
links:
  officialDocument:
    href: "https://example.org/usccb/nihil-obstat-document-2025.pdf"
    title: "USCCB Nihil Obstat Approval"
    type: "application/pdf"
  additionalNotes:
    href: "https://example.org/usccb/notes/2025-review"
    title: "Detailed Review Notes"
    type: "text/html"

```

Multiple Instances of evaluations may be appropriate for each text, and thus be child items in an array object type ```EcclesiasticalEvaluations``` property on the parent data object.

##### Legal Domain Discussion and Exploration

The Legal Domain focuses on the recognition, licensing, and broader intellectual property considerations of biblical texts. Different jurisdictions and international conventions can affect the distribution, modification, and usage of various versions of the Bible. As there are different jurisdictions and conventions across the Globe, we will need to consider the scope and scale of various relevant regulatory bodies in the legal domain.

###### Legal Governing Bodies Considered
Most sovereign nations maintain at least one official body (office, bureau, or ministry) dedicated to intellectual property oversight. Each country may have unique laws or regulations for registering copyrights, defining fair use/fair dealing, and handling disputes. Additionally, **regional frameworks** (like the African Regional Intellectual Property Organization, ARIPO, or the European Patent Office, EPO) can coordinate IP matters among member states. Countries often share or adopt common frameworks through international treaties (like the Berne Convention).

**World Intellectual Property Organization (WIPO)**
   - **Scope**: International treaties (e.g., Berne Convention) that standardize or coordinate copyright protections across multiple countries.
   - **Relevance**: Sets the universal baseline for copyright, public domain, and licensing statuses recognized among member states.
   - **Website**: [wipo.int](https://www.wipo.int)


###### National and Regional Intellectual Property Offices
Each country's national IP office or courts handle infringement cases according to local laws.

If an individual or company in one country infringes upon the IP rights of another country’s citizen, enforcement usually requires collaboration between the involved governments or leveraging international agreements. But ultimately, each nation independently decides how (or if) to enforce intellectual property laws within its own territory.

There are also regional offices which coordinate between nations in particular geographic zones, but they often work with member states rather than enforce directly.

**Regional Bodies**
| Juridical Region                           | Office Name                                                                | Approximate Citizens | Data Source URL                                    | Date Accessed |
|--------------------------------------------|----------------------------------------------------------------------------|----------------------|----------------------------------------------------|---------------|
| Africa (English-speaking)                  | African Regional Intellectual Property Organization (ARIPO)                | 280 million          | [ARIPO](https://www.aripo.org)                     | 2025-03-18    |
| Africa (French-speaking)                   | African Intellectual Property Organization (OAPI)                          | 190 million          | [OAPI](http://www.oapi.int)                        | 2025-03-18    |
| Andean Community                           | Andean Community Intellectual Property Office (CAN)                        | 115 million          | [CAN](https://www.comunidadandina.org)             | 2025-03-18    |
| Benelux Region                             | Benelux Office for Intellectual Property (BOIP)                            | 30 million           | [BOIP](https://www.boip.int/en)                    | 2025-03-18    |
| Eurasian Region                            | Eurasian Patent Organization (EAPO)                                        | 220 million          | [EAPO](https://www.eapo.org)                       | 2025-03-18    |
| European Union                             | European Union Intellectual Property Office (EUIPO)                        | 447 million          | [EUIPO](https://euipo.europa.eu)                   | 2025-03-18    |
| Europe (Extended beyond EU)                | European Patent Office (EPO)                                               | 700 million          | [EPO](https://www.epo.org)                         | 2025-03-18    |
| Middle East (Gulf Cooperation Council)     | Gulf Cooperation Council Patent Office (GCCPO)                             | 60 million           | [GCCPO](https://www.gccpo.org)                     | 2025-03-18    |
| Eastern Caribbean                          | Organisation of Eastern Caribbean States Intellectual Property Office (OECS IPO) | 600 thousand         | [OECS IPO](https://oecs.org)                       | 2025-03-18    |


**National Bodies**
| Juridical Zone | Controlling National Office                                  | Data Source URL                                                                                 | Example Bible Versions                                                                                             |
|----------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Vatican City   | Vatican Apostolic Library / Holy See                         | [Vatican.va](https://www.vatican.va)                                                            | Nova Vulgata, Editio Typica Tertia (official Latin Catholic Bible)                                                  |
| United States  | United States Copyright Office (USCO)                        | [USCO](https://www.copyright.gov)                                                               | NIV, ESV, NLT, NASB, NKJV, NABRE (Catholic), RSV-CE (Catholic), Orthodox Study Bible (Eastern Orthodox)            |
| United Kingdom | Intellectual Property Office (UK IPO)                        | [UK IPO](https://www.gov.uk/government/organisations/intellectual-property-office)              | NRSV, REB, Jerusalem Bible (Catholic), New Jerusalem Bible (Catholic)                                              |
| Canada         | Canadian Intellectual Property Office (CIPO)                 | [CIPO](https://www.ic.gc.ca/eic/site/cipointernet-internetopic.nsf/eng/home)                    | NRSVue, NLT-CE (Catholic), Revised Standard Version Canadian Catholic Edition (RSV-CCE)                            |
| Russia         | Federal Service for Intellectual Property (Rospatent)        | [Rospatent](https://rospatent.gov.ru/en)                                                        | Synodal Translation (Russian Orthodox Bible)                                                                        |
| Greece         | Hellenic Industrial Property Organisation (OBI)              | [OBI](https://www.obi.gr/en/)                                                                   | Greek Orthodox New Testament                                                                                       |

###### Non-Government Organizations

| Organization                                              | Role and Scope                                                                                          | Data Source URL                                              | Example Bible Versions or Texts                                     |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------|
| Vatican Apostolic Library                                 | Vatican repository preserving manuscripts, ancient biblical texts, and significant historical documents.| [vatlib.it](https://www.vatlib.it/home.php?ling=eng)         | Codex Vaticanus, Nova Vulgata, historical biblical manuscripts       |
| Libreria Editrice Vaticana (LEV)                          | Official publishing house of the Holy See, publishing authoritative Catholic texts and translations.    | [lev.va](https://www.libreriaeditricevaticana.va)            | Nova Vulgata, official liturgical texts and documents                |
| Pontifical Biblical Institute (Biblicum)                  | Advanced biblical scholarship, critical texts, commentaries, and research resources.                    | [biblico.it](https://www.biblico.it)                         | Scholarly biblical commentaries and critical editions                |
| École Biblique et Archéologique Française de Jérusalem (EBAF) | Dominican research institute producing biblical archaeology and scholarly biblical translations.         | [ebaf.edu](https://www.ebaf.edu)                             | Jerusalem Bible, scholarly biblical archaeology resources            |
| Catholic Biblical Federation (CBF)                        | Global Catholic network promoting biblical pastoral ministry, translations, and biblical resources.     | [c-b-f.org](https://www.c-b-f.org)                           | Various local translations, pastoral biblical materials              |
| Project Gutenberg                                         | Digital library offering public domain texts, including historic Bible translations freely available online. | [gutenberg.org](https://www.gutenberg.org)                   | King James Version (KJV), Douay-Rheims Bible, Geneva Bible           |
| Internet Archive                                          | Repository preserving and providing free access to historical texts, manuscripts, and scanned Bible editions. | [archive.org](https://archive.org)                           | King James Version (KJV), various scanned historical Bible editions  |
| Creative Commons                                          | Provides standardized, globally recognized open licensing frameworks.                                   | [creativecommons.org](https://creativecommons.org)           | World English Bible (WEB), Open English Bible (OEB), various commentaries and devotional resources |
| Center for the Study of New Testament Manuscripts (CSNTM) | Digitizes and freely shares high-resolution images of Greek New Testament manuscripts.                  | [csntm.org](https://csntm.org)                               | Digitized ancient Greek New Testament manuscripts                    |
| Society of Biblical Literature (SBL)                      | Scholarly resources, critical editions, openly licensed biblical texts and standardized formats.        | [sbl-site.org](https://www.sbl-site.org)                     | SBL Greek New Testament, Hebrew Bible Critical Editions              |
| Digital Bible Library (DBL)                               | Digital library of verified biblical texts provided by global translation organizations.                | [digitalbiblelibrary.org](https://digitalbiblelibrary.org)   | Hundreds of modern Bible translations and audio Bibles               |
| Unbound Bible (Biola University)                          | Comprehensive digital repository of free Bible translations and texts in many languages.                | [unbound.biola.edu](https://unbound.biola.edu)               | Many public domain translations across diverse languages             |
| Open Scriptures Project                                   | Community-driven open-source initiative providing tools, standards, and openly licensed biblical texts. | [openscriptures.org](http://openscriptures.org)              | Open scripture data sets, collaborative text standardization efforts |

##### Legal Domain Data Structure Discussion

Within the legal domain, various aspects must be considered regarding any given Scriptural text. 

First, we must conside the custodial lineage of the digital asset itself--such as the custodial chain and the organization responsible for digitizing it, source materials, etc. This may be necessary to evaluate what legal obligations one may inadvertantly incur by trusting an unreliable source that claims a work is public domain, when it is in fact under IP license/copyright (such as a pirated copy being distributed).

Second, we need to consider what licensing model is attached to the work (e.g. MIT License, Copyright, etc.), and the details about the licensing custodial organization, the license details (identifier, links, etc.), and associated dates (copyright year, limited time license durations, etc.).

Third, we need to consider the Juridical authority or authorities in scope based on the custodial chain (e.g. a version original published in the US, and then digitized by a University in Germany).

##### Legal Domain Data Entity Structure

This secition outlines the structured data model for representing the legal custody lineage of Scriptural (or related) texts. It is composed of several **entities** (objects) and one **enumeration**. Each entity has a corresponding data dictionary. All dates must use the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (e.g., `YYYY-MM-DD`), and jurisdictions should use [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes or recognized regional codes (e.g., `EU`).

**CustodialRecord**

Represents a single stage in the chain of custody for a text.

| Field Name         | Type      | Required? | Description                                                                                                                                     |
|--------------------|-----------|----------:|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **custodianName**  | String    | **Yes**   | Organization or individual holding custody (e.g., “Global Bible Archives”).                                                                     |
| **custodianType**  | String    | **Yes**   | **Enumeration**  indicating role of this custodian (e.g., “Publisher”, “Digitizer”).     |
| **jurisdiction**   | Object    | **Yes**   | A **Jurisdiction** object specifying the ISO country code or region, plus an **OfficeRecord** if relevant.|
| **custodyDetails** | Object    | **Yes**   | A **CustodyDetails**object describing timeline and scope of custody.                                                      |
| **sourceMaterial** | Object    | **Yes**   | A **SourceMaterial** object describing the content.                                                                        |
| **license**        | Object?   | Optional  | A **License** object, if a specific license applies at this custodial stage;  omitted if unknown                           |

**OfficeRecord**

| Field Name       | Type        | Required? | Description                                                                        |
|------------------|-------------|----------:|------------------------------------------------------------------------------------|
| **name**         | String      | **Yes**   | Official name of the office/authority, e.g., “UK Intellectual Property Office.”    |
| **address**      | String      | Optional  | Physical or mailing address.                                                       |
| **url**          | String (URL)| Optional  | Official website URL, e.g., “https://www.gov.uk/government/organisations/intellectual-property-office”. |
| **phone**        | String      | Optional  | Main contact phone number, ideally in [E.164 format](https://en.wikipedia.org/wiki/E.164). |
| **contactEmail** | String (Email) | Optional| General/public contact email address.                                              |

**CustodyDetails**

| Field Name           | Type                | Required? | Description                                                                                                                 |
|----------------------|---------------------|----------:|-----------------------------------------------------------------------------------------------------------------------------|
| **custodyStartDate** | String (Date)      | **Yes**   | Start date of custody in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, e.g., “2005-07-01”.                    |
| **custodyEndDate**   | String (Date) or null | Optional| End date of custody, in ISO 8601 format. `null` if ongoing.                                                                |
| **notes**            | String             | Optional  | Free-form notes describing relevant activities (digitization, archiving, distribution, etc.) during this custodial period. |

**SourceMaterial**

| Field Name        | Type         | Required? | Description                                                                                    |
|-------------------|-------------:|----------:|------------------------------------------------------------------------------------------------|
| **description**   | String       | **Yes**   | Brief textual description of the material, e.g., “High-resolution scans from a 1611 KJV edition.” |
| **referenceLink** | String (URL) | Optional  | URL pointing to more detailed documentation or metadata about the source material.             |

**License**

| Field Name            | Type                     | Required?   | Description                                                                                                |
|-----------------------|--------------------------|------------:|------------------------------------------------------------------------------------------------------------|
| **licenseId**       | String     | **Yes**     | Explicit unique identifier denoting the license (for Copyrighted works, "Copyright" should be used, otherwise a unique identifier for the various other license types)           |
| **licenseURL**        | String (URL)             | Optional    | Link to official license text or webpage for the license.                                                  |
| **licenseStartDate**  | String (Date)            | Optional    | Date the license took effect, in ISO 8601 format.                                                           |
| **licenseEndDate**    | String (Date) or null    | Optional    | Expiry date if limited; `null` if perpetual or unspecified.                                                |
| **rightsHolder**      | String                   | Optional    | Name of the individual or organization legally holding the IP rights or granting the license.              |

**CustodialRecord**

| Field Name         | Type      | Required? | Description                                                                                                                |
|--------------------|-----------|----------:|----------------------------------------------------------------------------------------------------------------------------|
| **custodianName**  | String    | **Yes**   | Organization or individual holding custody (e.g., “University of Oxford Digital Archives”).                                |
| **custodianType**  | String    | **Yes**   | Must be a value from the [custodianType Enumeration](#custodiantype-enumeration).                                          |
| **jurisdiction**   | Object    | **Yes**   | A **Jurisdiction** object with ISO country/region code + optional [OfficeRecord](#data-dictionary-officerecord).           |
| **custodyDetails** | Object    | **Yes**   | A **CustodyDetails** object describing the timeline and scope of this custodial stage.                                     |
| **sourceMaterial** | Object    | **Yes**   | A **SourceMaterial** object describing the material handled or digitized.                                                  |
| **license**        | Object?   | Optional  | A **License** object if applicable, indicating licensing terms at this custodial stage.                                    |

**custodianType Enumeration**

| Value                 | Description                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Publisher**         | Entity that produces and issues printed or digital works.                                                                   |
| **Digitizer**         | Entity responsible for converting physical material (books, manuscripts) to digital form.                                  |
| **Distributor**       | Entity engaged in distributing or disseminating a resource (online platform, library, etc.).                                |
| **Archive**           | Organization that stores and preserves documents, manuscripts, or records in a long-term capacity.                         |
| **Repository**        | Specialized collection or database holding digital resources.                                                               |
| **AcademicInstitution** | University, college, or scholarly institute that digitizes or holds custody of texts.                                     |
| **ReligiousInstitution** | Church, diocese, denominational body, or similar organization overseeing religious texts.                                |
| **GovernmentOffice**  | Government or public institution with official custody (e.g., national archive).                                            |
| **RightsHolder**      | The legal owner of the intellectual property rights.                                                                        |
| **Individual**        | A private person (e.g., personal collection).                                                                               |
| **Other**             | Catch-all category for a custodian type not defined in the above enumeration.                                               |

**JSON Made-up example**
```json
{
  "custodyChain": [
    {
      "custodianName": "Lancelot Charles Lee Brenton",
      "custodianType": "Publisher",
      "jurisdiction": {
        "juridicalZone": "GB",
        "governingOffice": {
          "name": "UK Intellectual Property Office",
          "address": "Concept House, Cardiff Road, Newport, NP10 8QQ",
          "url": "https://www.gov.uk/government/organisations/intellectual-property-office"
        }
      },
      "custodyDetails": {
        "custodyStartDate": "1851-01-01",
        "custodyEndDate": "1900-12-31",
        "notes": "Original publication of Brenton's English translation of the Septuagint."
      },
      "sourceMaterial": {
        "description": "First print edition of Lancelot C. L. Brenton's Septuagint, published in London.",
        "referenceLink": "https://en.wikipedia.org/wiki/Brenton%27s_English_Translation_of_the_Septuagint"
      },
      "license": {
        "licenseId": "Copyright",
        "licenseURL": "https://example.org/uk-copyright-law-of-the-period",
        "licenseStartDate": "1851-01-01",
        "licenseEndDate": "1923-01-01",
        "rightsHolder": "Estate of Lancelot Charles Lee Brenton"
      }
    },
    {
      "custodianName": "Internet Archive",
      "custodianType": "Digitizer",
      "jurisdiction": {
        "juridicalZone": "US",
        "governingOffice": {
          "name": "United States Copyright Office",
          "url": "https://www.copyright.gov"
        }
      },
      "custodyDetails": {
        "custodyStartDate": "2005-07-01",
        "custodyEndDate": "2010-01-01",
        "notes": "Scanned original copy and produced a freely downloadable digital version."
      },
      "sourceMaterial": {
        "description": "High-resolution scan of the 1851 print edition.",
        "referenceLink": "https://archive.org/details/BrentonSeptuagint_1851"
      },
      "license": {
        "licenseId": "PublicDomain",
        "licenseURL": "https://creativecommons.org/publicdomain/mark/1.0/",
        "licenseStartDate": "2005-07-01",
        "licenseEndDate": null,
        "rightsHolder": "None (public domain text)"
      }
    },
    {
      "custodianName": "OpenSeptuagintProject.org",
      "custodianType": "Repository",
      "jurisdiction": {
        "juridicalZone": "US",
        "governingOffice": {
          "name": "United States Copyright Office",
          "address": "101 Independence Ave S.E., Washington, D.C. 20559-6000",
          "url": "https://www.copyright.gov",
          "phone": "+1 202-707-3000",
          "contactEmail": "ask@copyright.gov"
        }
      },
      "custodyDetails": {
        "custodyStartDate": "2010-06-01",
        "custodyEndDate": null,
        "notes": "Hosting digitized copy and text files with updated formatting and corrections."
      },
      "sourceMaterial": {
        "description": "Digitally refined text version derived from Internet Archive scans.",
        "referenceLink": "https://openseptuagintproject.org/brenton-files"
      },
      "license": {
        "licenseId": "PublicDomain",
        "licenseURL": "https://creativecommons.org/publicdomain/mark/1.0/",
        "licenseStartDate": "2010-06-01",
        "licenseEndDate": null,
        "rightsHolder": "None (public domain content)"
      }
    }
  ]
}
```

**YAML Made-up example**
```yaml
custodyChain:
  # 1) Original 1851 Publication
  - custodianName: "Lancelot Charles Lee Brenton"
    custodianType: "Publisher"
    jurisdiction:
      juridicalZone: "GB"
      governingOffice:
        name: "UK Intellectual Property Office"
        address: "Concept House, Cardiff Road, Newport, NP10 8QQ"
        url: "https://www.gov.uk/government/organisations/intellectual-property-office"
    custodyDetails:
      custodyStartDate: "1851-01-01"
      custodyEndDate: "1900-12-31"
      notes: "Original publication of Brenton's English translation of the Septuagint."
    sourceMaterial:
      description: "First print edition of Lancelot C. L. Brenton's Septuagint, published in London."
      referenceLink: "https://en.wikipedia.org/wiki/Brenton%27s_English_Translation_of_the_Septuagint"
    license:
      licenseId: "Copyright"
      licenseURL: "https://example.org/uk-copyright-law-of-the-period"
      licenseStartDate: "1851-01-01"
      licenseEndDate: "1923-01-01"  # Illustrative date indicating expiration, for example's sake.
      rightsHolder: "Estate of Lancelot Charles Lee Brenton"

  # 2) Digitization by Internet Archive
  - custodianName: "Internet Archive"
    custodianType: "Digitizer"
    jurisdiction:
      juridicalZone: "US"
      governingOffice:
        name: "United States Copyright Office"
        url: "https://www.copyright.gov"
    custodyDetails:
      custodyStartDate: "2005-07-01"
      custodyEndDate: "2010-01-01"
      notes: "Scanned original copy and produced a freely downloadable digital version."
    sourceMaterial:
      description: "High-resolution scan of the 1851 print edition."
      referenceLink: "https://archive.org/details/BrentonSeptuagint_1851"
    license:
      licenseId: "PublicDomain"
      licenseURL: "https://creativecommons.org/publicdomain/mark/1.0/"
      licenseStartDate: "2005-07-01"
      licenseEndDate: null
      rightsHolder: "None (public domain text)"

  # 3) Repository / Distribution by OpenSeptuagintProject.org
  - custodianName: "OpenSeptuagintProject.org"
    custodianType: "Repository"
    jurisdiction:
      juridicalZone: "US"
      governingOffice:
        name: "United States Copyright Office"
        address: "101 Independence Ave S.E., Washington, D.C. 20559-6000"
        url: "https://www.copyright.gov"
        phone: "+1 202-707-3000"
        contactEmail: "ask@copyright.gov"
    custodyDetails:
      custodyStartDate: "2010-06-01"
      custodyEndDate: null
      notes: "Hosting digitized copy and text files with updated formatting and corrections."
    sourceMaterial:
      description: "Digitally refined text version derived from Internet Archive scans."
      referenceLink: "https://openseptuagintproject.org/brenton-files"
    license:
      licenseId: "PublicDomain"
      licenseURL: "https://creativecommons.org/publicdomain/mark/1.0/"
      licenseStartDate: "2010-06-01"
      licenseEndDate: null
      rightsHolder: "None (public domain content)"
```

The order of the records in the CustodyChain array should match the order of custodians as custody is transfered (in relevant key events at least).