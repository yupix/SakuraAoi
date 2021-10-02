from typing import Any, List, Optional

from pydantic import BaseModel


class User(BaseModel):
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    avatar_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None


class Comment(BaseModel):
    url: str
    html_url: str
    issue_url: str
    id: int
    node_id: str
    user: User
    created_at: str
    updated_at: str
    author_association: str
    body: str
    performed_via_github_app: Any


class Config(BaseModel):
    content_type: Optional[str] = None
    insecure_ssl: Optional[str] = None
    url: Optional[str] = None


class LastResponse(BaseModel):
    code: Optional[Any] = None
    status: Optional[Optional[str]] = None
    message: Optional[Optional[Any]] = None


class Hook(BaseModel):
    type: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    events: Optional[List[str]] = None
    config: Optional[Config] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None
    url: Optional[str] = None
    test_url: Optional[str] = None
    ping_url: Optional[str] = None
    deliveries_url: Optional[str] = None
    last_response: Optional[LastResponse] = None


class Owner(BaseModel):
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    avatar_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None


class License(BaseModel):
    key: Optional[str] = None
    name: Optional[str] = None
    spdx_id: Optional[str] = None
    url: Optional[Any] = None
    node_id: Optional[str] = None


class Repository(BaseModel):
    id: Optional[int] = None
    node_id: Optional[str] = None
    name: Optional[str] = None
    full_name: Optional[str] = None
    private: Optional[bool] = None
    owner: Optional[Owner] = None
    html_url: Optional[str] = None
    description: Optional[str] = None
    fork: Optional[bool] = None
    url: Optional[str] = None
    forks_url: Optional[str] = None
    keys_url: Optional[str] = None
    collaborators_url: Optional[str] = None
    teams_url: Optional[str] = None
    hooks_url: Optional[str] = None
    issue_events_url: Optional[str] = None
    events_url: Optional[str] = None
    assignees_url: Optional[str] = None
    branches_url: Optional[str] = None
    tags_url: Optional[str] = None
    blobs_url: Optional[str] = None
    git_tags_url: Optional[str] = None
    git_refs_url: Optional[str] = None
    trees_url: Optional[str] = None
    statuses_url: Optional[str] = None
    languages_url: Optional[str] = None
    stargazers_url: Optional[str] = None
    contributors_url: Optional[str] = None
    subscribers_url: Optional[str] = None
    subscription_url: Optional[str] = None
    commits_url: Optional[str] = None
    git_commits_url: Optional[str] = None
    comments_url: Optional[str] = None
    issue_comment_url: Optional[str] = None
    contents_url: Optional[str] = None
    compare_url: Optional[str] = None
    merges_url: Optional[str] = None
    archive_url: Optional[str] = None
    downloads_url: Optional[str] = None
    issues_url: Optional[str] = None
    pulls_url: Optional[str] = None
    milestones_url: Optional[str] = None
    notifications_url: Optional[str] = None
    labels_url: Optional[str] = None
    releases_url: Optional[str] = None
    deployments_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    pushed_at: Optional[str] = None
    git_url: Optional[str] = None
    ssh_url: Optional[str] = None
    clone_url: Optional[str] = None
    svn_url: Optional[str] = None
    homepage: Optional[str] = None
    size: Optional[int] = None
    stargazers_count: Optional[int] = None
    watchers_count: Optional[int] = None
    language: Optional[str] = None
    has_issues: Optional[bool] = None
    has_projects: Optional[bool] = None
    has_downloads: Optional[bool] = None
    has_wiki: Optional[bool] = None
    has_pages: Optional[bool] = None
    forks_count: Optional[int] = None
    mirror_url: Optional[Any] = None
    archived: Optional[bool] = None
    disabled: Optional[bool] = None
    open_issues_count: Optional[int] = None
    license: Optional[License] = None
    allow_forking: Optional[bool] = None
    forks: Optional[int] = None
    open_issues: Optional[int] = None
    watchers: Optional[int] = None
    default_branch: Optional[str] = None


class Label(BaseModel):
    id: Optional[int] = None
    node_id: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None
    default: Optional[bool] = None
    description: Optional[str] = None


class Assignee(BaseModel):
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    avatar_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None


class Assignee1(BaseModel):
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    avatar_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None


class Issue(BaseModel):
    url: Optional[str] = None
    repository_url: Optional[str] = None
    labels_url: Optional[str] = None
    comments_url: Optional[str] = None
    events_url: Optional[str] = None
    html_url: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    number: Optional[int] = None
    title: Optional[str] = None
    user: Optional[User] = None
    labels: Optional[List[Label]] = None
    state: Optional[str] = None
    locked: Optional[bool] = None
    assignee: Optional[Assignee] = None
    assignees: Optional[List[Assignee1]] = None
    milestone: Optional[Any] = None
    comments: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    closed_at: Optional[str] = None
    author_association: Optional[str] = None
    active_lock_reason: Optional[Any] = None
    body: Optional[str] = None
    timeline_url: Optional[str] = None
    performed_via_github_app: Optional[Any] = None


class Sender(BaseModel):
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    avatar_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None

class Head(BaseModel):
    label: str
    ref: str
    sha: str
    user: User

class Base(BaseModel):
    label: str
    ref: str
    sha: str
    user: User

class Self(BaseModel):
    href: str


class Html(BaseModel):
    href: str


class IssueLink(BaseModel):
    href: str


class Comments(BaseModel):
    href: str


class ReviewComments(BaseModel):
    href: str


class ReviewComment(BaseModel):
    href: str


class Commits(BaseModel):
    href: str


class Statuses(BaseModel):
    href: str

class Links(BaseModel):
    self: Self
    html: Html
    issue: IssueLink
    comments: Comments
    review_comments: ReviewComments
    review_comment: ReviewComment
    commits: Commits
    statuses: Statuses


class MergedBy(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool

class PullRequest(BaseModel):
    url: str
    id: int
    node_id: str
    html_url: str
    user: Optional[User] = None
    diff_url: str
    patch_url: str
    issue_url: str
    number: int
    state: str
    locked: bool
    title: str
    body: str
    created_at: str
    updated_at: str
    closed_at: str
    merged_at: str
    merge_commit_sha: str
    assignee: Any
    assignees: List
    requested_reviewers: List
    requested_teams: List
    labels: List[Label]
    milestone: Any
    draft: bool
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    head: Head
    base: Base
    _links: Links
    author_association: str
    auto_merge: Any
    active_lock_reason: Any
    merged: bool
    mergeable: Any
    rebaseable: Any
    mergeable_state: str
    merged_by: MergedBy
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int

class Author(BaseModel):
    name: str
    email: str
    username: str

class Committer(BaseModel):
    name: str
    email: str
    username: str


class Commit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Author
    committer: Committer
    added: List[str]
    removed: List
    modified: List[str]

class HeadCommit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: str
    author: Author
    committer: Committer
    added: List[str]
    removed: List
    modified: List[str]

class Pusher(BaseModel):
    name: str
    email: str

class GitWebHook(BaseModel):
    before: Optional[str] = None
    after: Optional[str] = None
    action: Optional[str] = None
    issue: Optional[Issue] = None
    comment: Optional[Comment] = None
    zen: Optional[str] = None
    hook_id: Optional[int] = None
    hook: Optional[Hook] = None
    repository: Optional[Repository] = None
    sender: Optional[Sender] = None
    pull_request: Optional[PullRequest] = None
    commits: Optional[List[Commit]] = None
    head_commit: Optional[HeadCommit] = None
    pusher: Optional[Pusher] = None
    compare: Optional[str] = None
