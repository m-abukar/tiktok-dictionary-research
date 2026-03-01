# TikTok Dictionary - Multi-Source Terminology Validation Research

Academic research project for Computer Science dissertation at University of Warwick.

## Project Overview

This research develops a multi-source validation system for identifying emerging cultural terminology. The system combines Google Trends analysis (primary data source) with Reddit community validation to distinguish genuine cultural phenomena from temporary search anomalies.

## Research Question

How can cross-platform validation improve accuracy in detecting culturally significant emerging terminology compared to single-source approaches?

## Methodology

### Two-Layer Architecture

**Layer 1: Discovery (Google Trends API)**
- Primary data source for term discovery
- Identifies search terms with significant upward trends
- Provides quantitative metrics on search volume and velocity

**Layer 2: Validation (Reddit API)**
- Secondary validation layer confirming cultural significance
- Uses simple algorithmic analysis
- Validates whether trending searches reflect actual community usage
- Distinguishes cultural terminology from news events

### Reddit Validation Methodology

Reddit data collection uses **algorithmic analysis only**:

1. **Keyword Search**: Query subreddits for posts containing terms discovered via Google Trends
2. **Frequency Counting**: Count mentions across relevant communities
3. **Context Analysis**: Identify usage patterns (natural conversation vs. definitional questions)
4. **Cross-Validation**: Check presence across multiple relevant subreddits

**Important**: Reddit data is used for validation counting only.

## Reddit API Usage

### Scope
- **Subreddits**: r/TikTokCringe, r/OutOfTheLoop, r/GenZ, r/NoStupidQuestions, r/explainlikeimfive
- **Data collected**: Public post titles and text containing terminology
- **Frequency**: 3 times per week (Monday/Wednesday/Friday mornings)
- **Rate limit**: 40 requests per minute (within 60/min allowance)
- **Annual volume**: ~260,000 requests (minimal compared to commercial usage)

### What We DON'T Do
- No machine learning training on Reddit data
- No collection of user data, comments, or voting information
- No posting, commenting, or community interaction
- No real-time monitoring or excessive requests
- No storage of individual user information
- No tracking of user behavior

### What We DO
- Read public posts containing terminology identified by Google Trends
- Count frequency of term mentions (simple algorithmic counting)
- Identify context patterns using keyword matching
- Cross-validate across multiple subreddits for significance
- Aggregate statistics only (not individual post storage)

**Reddit's Role**: Provides validation context through algorithmic frequency analysis

## Data Privacy & Ethics

### Privacy Protection
- Only public post content collected (no private/deleted content)
- No user profiling, tracking, or demographic inference
- Aggregated statistics only (individual posts not permanently stored)
- Fully GDPR compliant (no personal data processing)
- Compliant with Reddit's Responsible Builder Policy

### Transparency
- Research methodology publicly documented
- Code available for peer review and verification
- Results published for public educational benefit
- Academic oversight through University of Warwick

### Responsible Use
- Rate limiting well within Reddit's guidelines (40/min vs 60/min limit)
- Randomized request delays to minimize server impact
- Respects robots.txt and API terms of service
- No commercial use or monetization
- Academic research purpose only

## Academic Context

- **Institution**: University of Warwick, Department of Computer Science
- **Project**: CS310 Individual Project (Undergraduate Dissertation)
- **Academic Year**: 2025-2026
- **Research Focus**: Multi-source validation methodologies for cultural terminology detection
- **Supervisor**: [Add if applicable]

## Technical Architecture

### Primary Stack
- **Google Trends**: Primary data source 
- **Reddit API**: Validation layer (algorithmic analysis only)
- **Backend**: Django REST Framework (Python)
- **Frontend**: React/Next.js (TypeScript)
- **Database**: PostgreSQL
- **Analysis**: Pandas, NumPy (for Google Trends data only)

### Data Flow
```
Google Trends API
    ↓
Trending term detection
    ↓
Reddit API validation (algorithmic counting)
    ↓
Cross-validation decision
    ↓
Educational dictionary database
```

## Research Outputs

### Academic Deliverables
- Undergraduate dissertation (May 2026)
- Methodology documentation
- Validation accuracy analysis
- Comparative effectiveness study

### Public Deliverables
- Free educational dictionary of cultural terminology
- Open research methodology documentation
- Academic findings published for community benefit

## Deployment Timeline

- **Research Phase**: February - March 2026 (Data collection and validation)
- **Development**: March - April 2026 (System refinement)
- **Public Launch**: April 2026 (Educational resource)
- **Dissertation Submission**: May 2026

## Ethical Compliance

This research adheres to:
- University of Warwick research ethics guidelines
- GDPR data protection regulations
- Reddit's Responsible Builder Policy
- Academic integrity standards

## Contact

For academic inquiries, verification, or collaboration:
- **GitHub**: [@m-abukar](https://github.com/m-abukar)
- **Institution**: University of Warwick, Department of Computer Science

## License

This code is provided for academic research transparency and peer review purposes. The educational dictionary application is maintained separately for dissertation assessment.

## Acknowledgments

This research is conducted under academic supervision at University of Warwick and complies with all university research ethics requirements.

---
